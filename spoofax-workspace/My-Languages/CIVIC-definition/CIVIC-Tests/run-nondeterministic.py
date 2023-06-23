import subprocess
import os
import shlex
import json
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from tqdm import tqdm
from scipy import stats
from helper_functions import run, select_files_with_extensions
import argparse
import pandas as pd
from os import listdir

N_ITERATIONS = 30
TEX_FOLDER = "latex"

def create_bar_chart(ref_stdout_list, funcon_runs, unique_outcomes, legend_labels, file, x_label):
    # Count the occurrences of each outcome for g++
    ref_counts = [ref_stdout_list.count(outcome) + 0.01 for outcome in unique_outcomes]

    # Count the occurrences of each outcome for each funcons run
    funcon_counts = []
    for funcon_stdout_list in funcon_runs:
        counts = [funcon_stdout_list.count(outcome) + 0.01 for outcome in unique_outcomes]
        funcon_counts.append(counts)

    # Sorting outcomes alphabetically and the corresponding counts
    sorted_indices = sorted(range(len(unique_outcomes)), key=lambda k: unique_outcomes[k])
    unique_outcomes = [unique_outcomes[i] for i in sorted_indices]
    ref_counts = [ref_counts[i] for i in sorted_indices]
    funcon_counts = [[counts[i] for i in sorted_indices] for counts in funcon_counts]

    x = np.arange(len(unique_outcomes))  # label locations
    width = 0.35  # width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, ref_counts, width, label='g++')
    legends = ['g++']

    for i, counts in enumerate(funcon_counts):
        rects = ax.bar(x + width/2, counts, width, label=legend_labels[i])
        legends.append(legend_labels[i])

    # Add some text for labels, title, and custom x-axis tick labels, etc.
    ax.set_ylabel('Frequency')
    ax.set_xlabel(x_label)
    ax.set_xticks(x)
    ax.set_xticklabels(unique_outcomes, rotation='vertical')
    ax.legend(legends)
    ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))

    plt.tight_layout()
    plt.savefig(f"{os.path.basename(file)}_bar_chart.png")
    plt.close()

def create_civ_file(file):
    with open(file + ".cpp", "r") as cpp_file:
        cpp_code = cpp_file.read()
        cpp_code = cpp_code.replace("#", "")
    
    with open(file + ".civ", "w") as civ_file:
        civ_file.write(cpp_code)

def func(f, run_tests=True, generate_graphs=True):   # Added run_tests and generate_graphs flags
    if run_tests:
       # Compile the C++ file once
        def compile(f):
            return_code, stdout, stderr = run(f"bash run_cpp_container_already_running.sh {f+'.cpp'}")
            if return_code != 0:
                print(stderr)
                return

        # Run the compiled binary multiple times
        ref_stdout_list = []
        # for _ in tqdm(range(N_ITERATIONS), desc="Running g++ iterations", unit="iterations"):
        for _ in range(N_ITERATIONS):
            compile(f)
            return_code, stdout, stderr = run("sudo docker exec -it cpp_container /bin/bash -c ./output")
            ref_stdout_list.append(stdout)
            if return_code != 0:
                print(stderr)
        
        # if os.path.exists(f + '.config'):
        #     config = f + '.config'
        # else:
        #     config = os.path.join(os.path.dirname(f), "default.config")
        # # print(f"{f} config   {config}")
        if os.path.exists(f + ".config.json"):

            with open(f + ".config.json") as file:
                data = json.load(file)
        else:
            return
        print(file, data)
        runs = data["runs"]
        x_label = data["x_label"]
        funcon_runs = []
        legend_labels = []
        print(f"doing {len(runs.items())} runs for {f}")

        for _, value in runs.items():
            funcon_stdout_list = []
            args = value['args']
            legend_label = value['legend_label']
            legend_labels.append(legend_label)

            for _ in range(N_ITERATIONS):

                seed = random.randint(0, 65535)
                code, stdout, stderr = run(f"/home/l/.cabal/bin/CIVIC-Runfct {args} --seed {seed} {f + '.fct'}")

                stdout = "".join(stdout)
                program_return = stdout.split("Result:\n")[-1].split("\n")[0]
                program_stdout = stdout.split("Output Entity: standard-out\n")[-1].split("\n")[0]
                string = "".join(program_stdout.split(",")).replace("[]","").replace('"', '').replace("\\n", "\n")

                funcon_stdout_list.append(string)
            funcon_runs.append(funcon_stdout_list)

        # Saving the stdout data to a json file
        test_data = {
            "ref_stdout_list": ref_stdout_list,
            "funcon_runs": funcon_runs
        }
        with open(f"{f}.json", "w") as file:
            json.dump(test_data, file)
    else:
        try:
            with open(f"{f}.json", "r") as file:
                data = json.load(file)
            ref_stdout_list = data["ref_stdout_list"]
            funcon_runs = data["funcon_runs"]
        except FileNotFoundError:
            print(f"No data found for {f}. Running tests again.")
            return func(f, run_tests=True, generate_graphs=generate_graphs)

    # Graph generation
    if generate_graphs:
        ref_unique_outcomes = list(set(ref_stdout_list))
        funcon_unique_outcomes = list(set().union(*funcon_runs))
        unique_outcomes = list(set(ref_unique_outcomes).union(set(funcon_unique_outcomes)))

        # create a bar char with g++ outcomes and each of the funcons runs.
        create_bar_chart(ref_stdout_list, funcon_runs, unique_outcomes, legend_labels, f, x_label)
        generate_tex_figure(f)

def generate_tex_figure(file):
    figure_string = "\\begin{figure}[H]\n\\centering\n\\includegraphics[width=\\textwidth]{" + \
                    f"{os.path.basename(file)}_bar_chart.png" + "}\n\\caption{" + \
                    f"Figure for {os.path.basename(file)}" + "}\n\\end{figure}\n"
    with open(f"{TEX_FOLDER}/{os.path.basename(file)}.tex", 'w') as tex_file:
        tex_file.write(figure_string)

def generate_tex_file():
    figures_tex = [f for f in listdir(TEX_FOLDER) if f.endswith('.tex')]
    with open(f"{TEX_FOLDER}/all_figures.tex", 'w') as all_figures_tex:
        all_figures_tex.write("\\documentclass{article}\n\\usepackage{graphicx}\n\\usepackage{float}\n\\begin{document}\n")
        for figure_tex in figures_tex:
            with open(f"{TEX_FOLDER}/{figure_tex}", 'r') as tex_content:
                all_figures_tex.write(tex_content.read() + "\n")
        all_figures_tex.write("\\end{document}")
    run(f"pdflatex -interaction=nonstopmode -output-directory={TEX_FOLDER} {TEX_FOLDER}/all_figures.tex")


def main(run_tests=True, generate_graphs=True):   # Added run_tests and generate_graphs flags

        DIR = 'nondeterministic-programs'
        files = select_files_with_extensions(f"{DIR}", ['.cpp'], include_subdirectories=False)
        print(files)
        for f in files:
            create_civ_file(f)

        run(f"bash regen-funcons.sh {DIR}")

        files = select_files_with_extensions(f"{DIR}", ['.cpp', '.fct', '.config.json'], include_subdirectories=False)
        print(files)
        for f in tqdm(files, desc="Processing files", unit="file"):
            func(f, run_tests=run_tests, generate_graphs=generate_graphs)   # Passing the flags to the func function

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-tests", dest="run_tests", action="store_true", help="Run tests")
    parser.add_argument("--no-run-tests", dest="run_tests", action="store_false", help="Do not run tests")
    parser.add_argument("--generate-graphs", dest="generate_graphs", action="store_true", help="Generate graphs")
    parser.add_argument("--no-generate-graphs", dest="generate_graphs", action="store_false", help="Do not generate graphs")

    parser.set_defaults(run_tests=True, generate_graphs=True)

    args = parser.parse_args()

    run(f"mkdir -p {TEX_FOLDER}")
    pwd = os.getcwd()
    print(run(f"sudo docker run --name cpp_container -v {pwd}:/usr/src/myapp -td gcc:latest"))

    main(run_tests=args.run_tests, generate_graphs=args.generate_graphs)

    generate_tex_file()

    print(run("sudo docker stop cpp_container"))
    print(run("sudo docker rm cpp_container"))
