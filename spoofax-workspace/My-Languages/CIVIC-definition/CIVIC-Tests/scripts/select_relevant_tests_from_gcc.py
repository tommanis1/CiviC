import os
import shutil
import argparse
import subprocess
import json
from helper_functions import run
def extract_classes_and_functions(summary_path):
    """
    Extracts class names and their associated member functions from a summary file.
    Discards namespace prefixes from class names.
    Returns a dictionary with the extracted information.
    """

    implemented = {"classes": {}}

    with open(summary_path, 'r') as file:
        lines = file.readlines()

    current_class = None

    for line in lines:
        line = line.strip()

        if line.startswith("Class Name:"):
            current_class = line.split("Class Name:")[1].strip().split("::")[-1]

            if current_class not in implemented["classes"]:
                implemented["classes"][current_class] = []

        elif line.startswith("Functions:") and current_class is not None:
            functions = line.split("Functions:")[1].strip().split(", ")
            implemented["classes"][current_class].extend(functions)

    # print(implemented)
    return implemented

def runp(cmd):
    r, o, e = run(cmd)
    if r : print(e)
def select_and_copy_files(implemented, gcc_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    classes = implemented["classes"].keys()

    for class_name in classes:
        class_path = os.path.join(gcc_folder, class_name)

        if os.path.exists(class_path):
            output_class = os.path.join(output_folder, class_name)
            os.makedirs(output_class, exist_ok=True)


            for root, _, files in os.walk(class_path):
                for file_name in files:
                    file_path = os.path.join(root, file_name)
                    if 'native_handle' in file_path:
                        continue

                    with open(file_path, 'r') as file:
                        if 'main' in file.read():
                            relative_path = os.path.relpath(file_path, class_path)
                            output_file_path = os.path.join(output_class, relative_path)
                            if not os.path.commonpath([output_file_path, output_class]) == output_class:
                                continue
                            os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
                            shutil.copy2(file_path, output_file_path)


    def count_files(f): return subprocess.run(f"find {f} -type f | wc -l", shell=True, capture_output=True, text=True).stdout.strip()
    with open(os.path.join(output_folder, "summary"), 'w') as summary_file:
        summary_file.write(f"Number of gcc thread tests: {count_files(gcc_folder)}\n")
        summary_file.write(f"Number of selected tests: {count_files(output_folder)}\n")

def main(project_folder, output_folder):
    summary_file = os.path.join(project_folder, 'summary')
    subprocess.run(['make'], cwd=project_folder, check=True)
    implemented = extract_classes_and_functions(summary_file)

    # Select and copy the relevant test files
    gcc_folder = "gcc/libstdc++v3/testsuite/30_threads/"
    output_folder = "relevant_tests_from_gcc"
    select_and_copy_files(implemented, gcc_folder, output_folder)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Select relevant tests from gcc")
    parser.add_argument('project_folder', type=str, help='The path of the project folder')
    parser.add_argument('output_folder', type=str, help='The path of the project folder')



    args = parser.parse_args()
    main(args.project_folder, args.output_folder)