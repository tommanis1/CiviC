import subprocess
import sys
import os
import re
import glob
import fnmatch
import shutil

def select_files_with_all_extensions(dir, extensions):
    matches = {}
    for root, _, filenames in os.walk(dir):
        for filename in filenames:
            name, ext = os.path.splitext(filename)
            if ext in extensions:
                if name not in matches:
                    matches[name] = set()
                matches[name].add(ext)
    result = [os.path.join(dir, name) for name, exts in matches.items() if exts == set(extensions)]
    return result

def run(cmd): 
    return subprocess.check_output(cmd.split(" ")).decode(sys.stdout.encoding)

def print_side_by_side(a, b):
    w, _ = shutil.get_terminal_size((80, 20))
    for i in range(max(len(a), len(b))):
        try:
            print(a[i], end="")
            l = len(a[i])
        except:
            l = 0
        try:
            print(" " * (w//2 - l),end="")
            print(b[i])
        except IndexError:
          print()

def compare(files):
    for f in files:
        # custom tests
        if 'thread-mutex-lock' in f:
            # print(run(f"bash run_cpp.sh {f + '.cpp'}"))
            print_side_by_side(run(f"bash run_cpp.sh {f + '.cpp'}").split("\n"), run(f"runfct --non-deterministic value-operations,rules,pattern-matching,interleaving-of-args {f + '.fct'}").split("\n"))
        elif 'thread-mutex-lock_unstable' in f:
            print_side_by_side(run(f"bash run_cpp.sh {f + '.cpp'}").split("\n"), run(f"runfct --non-deterministic value-operations,rules,pattern-matching,interleaving-of-args {f + '.fct'}").split("\n"))
        else:
            pass


def rm_exstension(files):
    return ["".join(f.split(".")[:-1]) for f in files]

if __name__ == "__main__":
    DIR = 'C++'
    try:
        print(run(f"bash regen-funcons.sh {DIR}"))
    except:
        pass
    files = select_files_with_all_extensions(DIR, ['.civ', '.cpp', '.fct'])
    print(files)
    compare(files)
