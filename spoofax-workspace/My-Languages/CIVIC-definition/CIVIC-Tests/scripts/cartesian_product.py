import itertools
import re
import datetime
import os
from helper_functions import select_files_with_extensions, run
import logging
import argparse

def get_logger(name, log_file, level=logging.INFO):
    """Create a logger object"""
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

    handler = logging.FileHandler(log_file)        
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

def create_cartesian_product_file(f, output_dir, logger):
    logger.info(f"start: {f}")
    program = open(f"{f}.cpp", 'r').read()
    split_on_main = re.split('(?:void|int)\smain[^{]*{', program)
    main_function = split_on_main[-1]

    split_end_main = main_function.split("}")
    main_body = "}".join(split_end_main[:-1]).replace("\n", "")

    lines = main_body.split(";")[:-1]
    combinations = list(itertools.product(lines, repeat=len(lines))) 
    # + [""]
    logger.info(f"len lines {len(lines)}")

    # logger.info(f"lines{lines}")
    logger.info(f"len combinations{len(combinations)}")
    for i, combo in enumerate(combinations):
        new_program = (
        """#include <iostream>\n"""
        + split_on_main[0]
        + re.findall(r'(?:void|int)\smain[^{]*{', program)[0]
        + "\n"
        + ";".join(combo)
        + split_end_main[-1]
        + ";\n"
        + "return 0;"
        + "}"
        )
        open(os.path.join(os.path.join(output_dir), os.path.basename(f)+ f"-{i}-.cpp"), 'w+').write(new_program)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run multiple iterations of tests")
    parser.add_argument('input_folder', type=str, help='Input folder path')
    parser.add_argument('data_folder', type=str, help='Output folder path')

    args = parser.parse_args()

    run(f"mkdir -p {os.path.join(args.data_folder, 'runs-cartesian')}")
    time_str = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    target = os.path.join(args.data_folder, "runs-cartesian", f"run-{time_str}")
    run(f"mkdir -p {target}")

    logger = get_logger(f"cpp", os.path.join(target, f"debug.log"))

    files = select_files_with_extensions(args.input_folder, [".cpp"], include_subdirectories=False)
    for f in files:
        create_cartesian_product_file(f, target, logger)

    for handler in logger.handlers:
            handler.close()
            logger.removeFilter(handler)