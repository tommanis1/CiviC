import os
import shutil
import argparse
import subprocess
import json
from helper_functions import run,select_files_with_extensions, get_logger, run_with_log

def create_civ_file(file):
    with open(file + "cc", "r") as cpp_file:
        cpp_code = cpp_file.read()
        cpp_code = cpp_code.replace("#", "")
    
    with open(file + ".civ", "w") as civ_file:
        civ_file.write(cpp_code)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create fct files for relevant tests from gcc")
    parser.add_argument('output_folder', type=str, help='The to the relevant tests')
    parser.add_argument('regen_funcons_script', type=str, help='regen_funcons_script')

    args = parser.parse_args()

    logger = get_logger(f"debug", os.path.join(args.output_folder, f"debug.log"))


    files = select_files_with_extensions(args.output_folder, ["cc"], True)
    for f in files:

        create_civ_file(f)
    run_with_log(f"bash {args.regen_funcons_script} {args.output_folder}", "To funcons", logger)
    print(len(files))
    print(len(select_files_with_extensions(args.output_folder, ["cc","civ", "fct"], True)))
    for handler in logger.handlers:
        handler.close()
        logger.removeFilter(handler)


