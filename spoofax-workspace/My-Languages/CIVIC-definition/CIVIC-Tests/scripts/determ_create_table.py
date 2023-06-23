import os
import re
import argparse
import filecmp
import difflib
import pandas as pd

def create_output_files(run_folder, number_iterations):
    output_files = []
    # Determine number of iterations    
    # Go through each test file in permutations directory
    permutations_folder = os.path.join(run_folder, "permutations")
    for test_file in os.listdir(permutations_folder):
        if test_file.endswith(".cpp"):
            test_dict = {"test_file": os.path.join(permutations_folder, test_file)}
            funcons_output = []
            cpp_output = []
            
            # Find the corresponding output files for each iteration
            for i in range(number_iterations):
                iteration_cpp_folder = os.path.join(run_folder, f'iteration-{i}-cpp')
                iteration_funcons_folder = os.path.join(run_folder, f'iteration-{i}-funcons')
                
                for output_file in os.listdir(iteration_cpp_folder):
                    if re.match(f"{test_file[:-4]}_output_cpp-{i}.txt", output_file):
                        cpp_output.append(os.path.join(iteration_cpp_folder, output_file))
                for output_file in os.listdir(iteration_funcons_folder):
                    if re.match(f"{test_file[:-4]}_output-{i}.txt", output_file):
                        funcons_output.append(os.path.join(iteration_funcons_folder, output_file))
                        
            test_dict["cpp"] = cpp_output
            test_dict["funcons"] = funcons_output
            output_files.append(test_dict)
    return output_files

def all_files_identical(file_list):
    # Checks whether all files in the provided list have identical content.
    if len(file_list) < 2:
        return True
    return all(filecmp.cmp(file_list[0], f, shallow=False) for f in file_list[1:])

def get_num_differences(file1, file2):
    # Returns the number of differences between two files.
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        diff = difflib.ndiff(f1.readlines(), f2.readlines())
    return sum(1 for _ in diff if _[0] in ['-', '+'])

def extract_highest_number(text):
    numbers = re.findall(r'count:(\d+)', text)
    if numbers:
        return max(map(int, numbers)) + 1 # numbers is zero indexed
    return 0

def count_body(text):
    split_on_main = re.split('(?:void|int)\smain[^{]*{', text)
    main_function = split_on_main[-1]

    split_end_main = main_function.split("}")
    main_body = "}".join(split_end_main[:-1]).replace("\n", "")

    lines = main_body.split(";")[:-1]
    return len(lines)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Make table")
    parser.add_argument('runs_folder', type=str, help='Runs folder path')
    parser.add_argument('latex_folder', type=str, help='Latex folder path')
    parser.add_argument('og_folder', type=str, help='Path to the folder with original files')


    args = parser.parse_args()
    # Select the latest folder
    run_folder = sorted([d for d in os.listdir(args.runs_folder) if d.startswith("run-")])[-1]
    run_folder = os.path.join(args.runs_folder, run_folder)
    number_iterations = max([int(d.split('-')[1]) for d in os.listdir(run_folder) if d.startswith("iteration-")]) + 1

    
    test_results = create_output_files(run_folder, number_iterations)
    accept, reject = [], []
    for result in test_results:
        cpp = result["cpp"]
        funcons = result["funcons"]
        
        # Check if all files in cpp and funcons have the same content
        if all_files_identical(cpp) and all_files_identical(funcons):
            accept.append(result)
        else:
            reject.append(result)
    
    print(len(accept), len(reject))

    data = []
    for result in accept:
        name = os.path.basename(result["test_file"]).replace("permutations_", "")
        
        # Take the first file, as all of them are the same,  from cpp and funcons and compare them
        cpp_file = result["cpp"][0]
        funcons_file = result["funcons"][0]
        num_diff = get_num_differences(cpp_file, funcons_file)

        with open(cpp_file, 'r') as file:
            content = file.read()
            len_body = extract_highest_number(content)
        
        with open(os.path.join(args.og_folder, name), 'r') as file:
            content = file.read()
            len_body_og = count_body(content)
        
        data.append((name.replace("_", "\_"), len_body_og, len_body, num_diff))

    # Create a DataFrame
    df = pd.DataFrame(data, columns=['Name', 'Length of the program ($l$)',
                                     'Length of the permutated program ($\leq2l(l!)$)', 'Number of Differences'])
    print(df)

    table_caption = "Summary of Test Differences"
    table_title = f"This table lists the number of differences in the test results. The " \
                  f"The tests were run {number_iterations} times to ascertain the determinism. " \
                  f"The number of tests that were rejected due to inconsistencies were {len(reject)}."

    # LaTeX document setup
    preamble = "\\documentclass{standalone}\n" \
               "\\usepackage{booktabs}\n" \
               "\\usepackage[margin=1in]{geometry}\n" \
               "\\usepackage{tabularx}\n" \
               "\\usepackage{subcaption}\n" \
               "\\begin{document}\n"

    # LaTeX document end
    ending = "\\end{document}"

    # Convert DataFrame to LaTeX table
    df_latex = df.to_latex(index=False, escape=False, column_format='|X|X|X|X|')
    df_latex = df_latex.replace("\\begin{tabular}", "\\begin{tabularx}{\\textwidth}")
    df_latex = df_latex.replace("\\end{tabular}", "\\end{tabularx}")
    df_latex = df_latex.replace("\\toprule", "\\hline\\hline")
    df_latex = df_latex.replace("\\midrule", "\\hline")
    df_latex = df_latex.replace("\\bottomrule", "\\hline\\hline")
    df_latex = "\\begin{center}\n" + "\\caption{" + table_caption + "}\n" + df_latex + "\\subcaption{" + table_title + "}" + "\\end{center}"

    # Combine all parts and write to file
    with open(os.path.join(args.latex_folder, "deterministic.tex"), 'w') as f:
        f.write(preamble + df_latex + ending)