import subprocess
import os
import shlex
from helper_functions import run, select_files_with_extensions
from tqdm import tqdm
from scipy import stats
import numpy as np
import random
import argparse
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
N_ITERATIONS = 10

def create_bar_chart(ref_stdout_list, funcon_stdout_list, file):
    unique_outcomes = list(set(ref_stdout_list).union(set(funcon_stdout_list)))
    
    # Count the occurrences of each outcome
    ref_counts = [ref_stdout_list.count(outcome) + 0.01 for outcome in unique_outcomes]
    funcon_counts = [funcon_stdout_list.count(outcome) + 0.01 for outcome in unique_outcomes]
    
    x = np.arange(len(unique_outcomes))  # label locations
    width = 0.35  # width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, ref_counts, width, label='g++ outcomes')
    rects2 = ax.bar(x + width/2, funcon_counts, width, label='funcons outcomes')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Frequency')
    # ax.set_title(f'Outcomes for {os.path.basename(file)}')
    ax.set_xticks(x)
    ax.set_xticklabels(unique_outcomes, rotation='vertical')
    ax.legend()
    ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))

    plt.tight_layout()
    plt.savefig(f"{os.path.basename(file)}_bar_chart.png")
    plt.close()

def create_tex_table(df, file_name, iterations):
    headers = " & ".join([header for header in df.columns])
    n_cols = len(df.columns)
    
    # Generate table's body
    rows = [" & ".join(map(str, row)) for row in df.values]
    table_body = "\\\\\n".join(rows[:-1]) + " \\\\\n" + rows[-1]

    # Escape special characters
    table_body = table_body.replace("_", "\\_")
    headers = headers.replace("_", "\\_")
    
    latex_document = f"""
    \\documentclass{{article}}
    \\usepackage{{tabularx}} % Required for tabularx
    \\usepackage{{booktabs}} % Provides \\toprule, \\midrule, \\bottomrule
    \\begin{{document}}
    % This is a comment. The table below shows the comparison between g++ and Funcons outcomes.
    \\begin{{table}}[h]
    \\centering
    \\caption{{Comparison between g++ and Funcons Outcomes for {iterations} iterations}} % Title
    \\label{{tab:nondeterm_comparison}} % Label
    \\begin{{tabularx}}{{\\textwidth}}{{*{{{n_cols}}}{{X}}}}
    \\toprule
    {headers} \\\\
    \\midrule
    {table_body} \\\\
    \\bottomrule
    \\end{{tabularx}}
    \\end{{table}}
    \\end{{document}}
    """

    with open(file_name, 'w') as f:
        f.write(latex_document)
def compile_tex_to_pdf(file_name):
    run(f'pdflatex -interaction=nonstopmode {file_name}')


def create_civ_file(file):
    with open(file + ".cpp", "r") as cpp_file:
        cpp_code = cpp_file.read()
        cpp_code = cpp_code.replace("#", "")
    
    with open(file + ".civ", "w") as civ_file:
        civ_file.write(cpp_code)

def func(f):
    # Compile the C++ file once
    return_code, stdout, stderr = run(f"bash run_cpp_container_already_running.sh {f+'.cpp'}")
    if return_code != 0:
        print(stderr)
        return

    # Run the compiled binary multiple times
    ref_stdout_list = []
    # for _ in tqdm(range(N_ITERATIONS), desc="Running g++ iterations", unit="iterations"):
    for _ in range(N_ITERATIONS):

        return_code, stdout, stderr = run("sudo docker exec -it cpp_container /bin/bash -c ./output")
        ref_stdout_list.append(stdout)
        if return_code != 0:
            print(stderr)
    funcon_stdout_list = []
    
    if os.path.exists(f + '.config'):
        config = f + '.config'
    else:
        config = os.path.join(os.path.dirname(f), "default.config")
    print(f"{f} config   {config}")

    # for _ in tqdm(range(N_ITERATIONS), desc="Running funcons iterations", unit="iterations"):
    for _ in range(N_ITERATIONS):

    # TODO make Runfct not hardcoded 
        seed = random.randint(0, 65535)
        code, stdout, stderr = run(f"/home/l/.cabal/bin/CIVIC-Runfct --non-deterministic value-operations,rules,pattern-matching,interleaving-of-args --seed {seed} {config} {f + '.fct'}")
        # print(stdout)

        stdout = "".join(stdout)
        program_return = stdout.split("Result:\n")[-1].split("\n")[0]
        program_stdout = stdout.split("Output Entity: standard-out\n")[-1].split("\n")[0]
        # print(program_stdout)
        string = "".join(program_stdout.split(",")).replace("[]","").replace('"', '').replace("\\n", "\n")

        # print(stdout.split("Result:"))

        # print(stdout.split("Result:"))
        # print("".join(stdout))
        # print("________________")
        # print(f)
        # print(code, stdout, stderr)
        # print("________________")
        # print(string)
        funcon_stdout_list.append(string)
    # ref_stdout_list.copy()
    # print(funcon_stdout_list)
    if len(funcon_stdout_list) == 0:
        return
    create_bar_chart(ref_stdout_list, funcon_stdout_list, f)
    print(len(funcon_stdout_list))
    print(funcon_stdout_list)
    print(ref_stdout_list)
    set_ref = set(ref_stdout_list)
    print(len(set_ref), set_ref)
    sef_funcons = set(funcon_stdout_list)
    print(len(sef_funcons), sef_funcons)

    n_total = len(set_ref.union(sef_funcons))
    print(len(set_ref.union(sef_funcons)), set_ref.union(sef_funcons))
    n_only_in_ref = len(set_ref.difference(sef_funcons))
    n_only_in_funcons =len(sef_funcons.difference(set_ref))
    n_shared = len(set_ref.intersection(sef_funcons))

    df = pd.DataFrame({
        'File': [os.path.basename(f)],
        'Different Outcomes': [n_total],
        'Outcomes only in g++': [n_only_in_ref],
        'Outcomes only in Funcons': [n_only_in_funcons],
        'Outcomes in both': [n_shared]
    })

    header = not os.path.exists('results.csv')
    df.to_csv('results.csv', mode='a', header=header, index=False)
    # print(f)
    # print(f"Different outcomes:{n_total}, Outcomes only in g++: {n_only_in_ref}, Outcomes only funcons: {n_only_in_funcons}, outcomes in both: {n_shared}")
    # print()
    # print(f, ":   ", len(list(set(ref_stdout_list))))
    # print(stats.kstest(np.array(ref_stdout_list), np.array(funcon_stdout_list)))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--table-only', action='store_true')
    parser.add_argument('--generate-only', action='store_true')
    args = parser.parse_args()

    # Default behavior when no arguments are given
    if not args.table_only and not args.generate_only:
        args.table_only = True
        args.generate_only = True

    # If generate-only flag is set, delete the existing results.csv file to start fresh
    if args.generate_only:
        if os.path.exists('results.csv'):
            os.remove('results.csv')

        DIR = 'nondeterministic-programs'
        files = select_files_with_extensions(f"{DIR}", ['.cpp'], include_subdirectories=False)

        for f in files:
            create_civ_file(f)

        run(f"bash regen-funcons.sh {DIR}")

        files = select_files_with_extensions(f"{DIR}", ['.cpp', '.fct'], include_subdirectories=False)
        for f in tqdm(files, desc="Processing files", unit="file"):
            func(f)

    if args.table_only:
        # Read the DataFrame from the CSV file
        df = pd.read_csv('results.csv')

        # Add headers to the DataFrame
        df.columns = ['File', 'Different Outcomes', 'Outcomes only in g++', 'Outcomes only in Funcons', 'Outcomes in both']

        # Create the .tex table
        create_tex_table(df, 'table.tex', N_ITERATIONS)

        # Compile the .tex file to a PDF
        compile_tex_to_pdf('table.tex')

if __name__ == "__main__":
    pwd = os.getcwd()
    print(run(f"sudo docker run --name cpp_container -v {pwd}:/usr/src/myapp -td gcc:latest"))
    # try:
    main()
    # except Exception as e:
    #     print(e)
    print(run("sudo docker stop cpp_container"))
    print(run("sudo docker rm cpp_container"))