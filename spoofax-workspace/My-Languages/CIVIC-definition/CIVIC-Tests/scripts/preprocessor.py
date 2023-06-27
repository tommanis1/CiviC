import argparse
import os
from pathlib import Path

def process_file(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()

    with open(file_path, "w") as f:
        for i, line in enumerate(lines, start=1):
            if line.strip() == '#include <testsuite_hooks.h>':
                f.write('#include <iostream>\n')
            elif 'VERIFY(' in line:
                line = line.replace('VERIFY(', 'do { if(!(')
                line = line.replace(')', ') { std::cout << "'+str(file_path)+'" << ":" << '+str(i)+' << ": Assertion failed.\\n"; } } while (false);')
            f.write(line)

def main():
    parser = argparse.ArgumentParser(description='Preprocess .cc files')
    parser.add_argument('dir', type=str, help='The directory to preprocess .cc files in')

    args = parser.parse_args()

    for path in Path(args.dir).rglob('*.cc'):
        process_file(path)

if __name__ == "__main__":
    main()