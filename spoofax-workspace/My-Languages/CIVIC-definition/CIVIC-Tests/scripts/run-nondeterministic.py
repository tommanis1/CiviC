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
from helper_functions import select_files_with_extensions, run
import argparse
import pandas as pd
from os import listdir
import datetime

def create_bar_chart(ref_stdout_list, funcon_runs, unique_outcomes, legend_labels, file, x_label, latex_folder):    # Count the occurrences of each outcome for g++
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

    plt.savefig(f"{os.path.join(latex_folder, os.path.basename(file))}_bar_chart.png")
    plt.close()

def create_civ_file(file):
    with open(file + ".cpp", "r") as cpp_file:
        cpp_code = cpp_file.read()
        cpp_code = cpp_code.replace("#", "")
    
    with open(file + ".civ", "w") as civ_file:
        civ_file.write(cpp_code)

def func(f, iterations, latex_folder, run_tests=True, generate_graphs=True):   
        container_name = f"cpp_container_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}_{random.randint(1000, 9999)}"
        return_code, stdout, stderr = run(f"docker run --name {container_name} -v {os.path.abspath('nondeterministic-programs')}:/usr/src/myapp -td test_cpp_image:latest")

        def compile(f):
            command = f"g++ -std=c++2b -o output /usr/src/myapp/{os.path.basename(f) + 'cpp'}"
            return_code, stdout, stderr = run(f"docker exec -it {container_name} /bin/bash -c '{command}'")
            if return_code != 0:
                print(stdout, stderr)
                return

        # Run the compiled binary multiple times
        ref_stdout_list = []
        # for _ in tqdm(range(N_ITERATIONS), desc="Running g++ iterations", unit="iterations"):
        for _ in range(iterations):
            compile(f)
            return_code, stdout, stderr = run(f"sudo docker exec -it {container_name} /bin/bash -c ./output")
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

            for _ in range(iterations):

                seed = random.randint(0, 65535)
                code, stdout, stderr = run(f"ulimit -Sv 4000000 && /home/l/.cabal/bin/CIVIC-Runfct {args} --seed {seed} {f + '.fct'}")

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
        # try:
        #     with open(f"{f}.json", "r") as file:
        #         data = json.load(file)
        #     ref_stdout_list = data["ref_stdout_list"]
        #     funcon_runs = data["funcon_runs"]
        # except FileNotFoundError:
        #     print(f"No data found for {f}. Running tests again.")
        #     return func(f, run_tests=True, generate_graphs=generate_graphs)

    # Graph generation  
    # if generate_graphs:
        ref_unique_outcomes = list(set(ref_stdout_list))
        funcon_unique_outcomes = list(set().union(*funcon_runs))
        unique_outcomes = list(set(ref_unique_outcomes).union(set(funcon_unique_outcomes)))
        create_bar_chart(ref_stdout_list, funcon_runs, unique_outcomes, legend_labels, f, x_label, latex_folder)

# def generate_tex_figure(file):
#     figure_string = "\\begin{figure}[H]\n\\centering\n\\includegraphics[width=\\textwidth]{" + \
#                     f"{os.path.basename(file)}_bar_chart.png" + "}\n\\caption{" + \
#                     f"Figure for {os.path.basename(file)}" + "}\n\\end{figure}\n"
#     with open(f"{TEX_FOLDER}/{os.path.basename(file)}.tex", 'w') as tex_file:
#         tex_file.write(figure_string)

# def generate_tex_file():
#     figures_tex = [f for f in listdir(TEX_FOLDER) if f.endswith('.tex')]
#     with open(f"{TEX_FOLDER}/all_figures.tex", 'w') as all_figures_tex:
#         all_figures_tex.write("\\documentclass{article}\n\\usepackage{graphicx}\n\\usepackage{float}\n\\begin{document}\n")
#         for figure_tex in figures_tex:
#             with open(f"{TEX_FOLDER}/{figure_tex}", 'r') as tex_content:
#                 all_figures_tex.write(tex_content.read() + "\n")
#         all_figures_tex.write("\\end{document}")
#     run(f"pdflatex -interaction=nonstopmode -output-directory={TEX_FOLDER} {TEX_FOLDER}/all_figures.tex")

        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run multiple iterations of the deterministic tests")
    parser.add_argument('n_iterations', type=int, help='Number of iterations')
    parser.add_argument('input_folder', type=str, help='Input folder path')
    parser.add_argument('dockerfile_dir', type=str, help='Dir with a Dockerfile')
    parser.add_argument('regen_funcons_script', type=str, help='regen_funcons_script')
    parser.add_argument('latex_folder', type=str, help='Path to dir for the generated latex code')
    args = parser.parse_args()

    run(f"mkdir -p {args.latex_folder}")
    print(run(f"docker build -t test_cpp_image:latest -f Dockerfile {os.path.abspath(args.dockerfile_dir)}"))

    files = select_files_with_extensions(f"{args.input_folder}", ['.cpp'], include_subdirectories=False)
    for f in files:
        create_civ_file(f)

    run(f"bash regen-funcons.sh {args.input_folder}")

    files = select_files_with_extensions(f"{args.input_folder}", ['.cpp', '.fct', '.config.json'], include_subdirectories=False)
    for f in tqdm(files, desc="Processing files", unit="file"):
        func(f, args.n_iterations, args.latex_folder, run_tests=True, generate_graphs=True)