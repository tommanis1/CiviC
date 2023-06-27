import itertools
import re
import os
import argparse
from helper_functions import select_files_with_extensions, run

# def generate_permutations(lst):
#     return [list(p) for p in permutations(lst)]

def create_permutation_files(f, target_dir):
    program = open(f"{f}.cpp", 'r').read()
    split_on_main = re.split('(?:void|int)\smain[^{]*{', program)
    main_function = split_on_main[-1]

    split_end_main = main_function.split("}")
    main_body = "}".join(split_end_main[:-1]).replace("\n", "")

    lines = main_body.split(";")[:-1]

    def try_catch(c, n):
        return f"try {{ std::cout << \"count:{c}\"; {n} ;}}" + f" catch (...) {{ std::cout << \"fail\" <<std::endl;}}"

    for i, perm in enumerate(itertools.permutations(lines)):
        new_stms = []
        count = 0
        for line in perm:
            new_stms.append(try_catch(count, line ))
            new_stms.append(try_catch(count+1, line ))
            count+=2

        permutations_program = (
            """#include <iostream>\n"""
            + split_on_main[0]
            + re.findall(r'(?:void|int)\smain[^{]*{', program)[0]
            + "\n"
            + ";\n".join(new_stms)
            + split_end_main[-1]
            + ";\n"
            + "return 0;"
            + "}"
        )
        path, filename = os.path.dirname(f), os.path.basename(f)

        open(os.path.join(os.path.join(target_dir), f"permutations_{i}_{filename}.cpp"), 'w+').write(permutations_program)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run multiple iterations of tests")
    parser.add_argument('input_folder', type=str, help='Input folder path')
    parser.add_argument('output_folder', type=str, help='Output folder path')

    args = parser.parse_args()

    run(f"mkdir -p {args.output_folder}")

    # Select all .cpp files and create permutation files
    files = select_files_with_extensions(args.input_folder, [".cpp"], include_subdirectories=False)
    for f in files:
        create_permutation_files(f, args.output_folder)