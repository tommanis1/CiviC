import subprocess
import sys
import os
import re
import glob
import shutil
import fnmatch
import shutil

super_permutations = [
"0",
"1",
"121",
"123121321",
"123412314231243121342132413214321",
"123451234152341253412354123145231425314235142315423124531243512431524312543121345213425134215342135421324513241532413524132541321453214352143251432154321",
"123456123451623451263451236451234651234156234152634152364152346152341652341256341253641253461253416253412653412356412354612354162354126354123654123145623145263145236145231645231465231425631425361425316425314625314265314235614235164235146235142635142365142315642315462315426315423615423165423124563124536124531624531264531246531243561243516243512643512463512436512431562431526431524631524361524316524312564312546312543612543162543126543121345621345261345216345213645213465213425613425163425136425134625134265134215634215364215346215342615342165342135642135462135426135421635421365421324561324516324513624513264513246513241563241536241532641532461532416532413562413526413524613524163524136524132564132546132541632541362541326541321456321453621453261453216453214653214356214352614352164352146352143652143256143251643251463251436251432651432156432154632154362154326154321654321"
]

"""void runUntilFixedPoint(int n, std::function<int()> f) {
    int prevResult;
    bool hasPrevResult = false;
    bool prevFail = false;
    bool isRunning = true;

    while (isRunning) {
        try {
            int result = f();
            if (!hasPrevResult || (prevResult != result)) {
                std::cout << n << ":" << result << std::endl;
                prevResult = result;
                hasPrevResult = true;
            } else {
                isRunning = false;
            }
            prevFail = false;
        } catch (const std::exception& e) {
            if (!hasPrevResult || !prevFail) {
                std::cout << n << ":" << "Fail" << std::endl;
                hasPrevResult = true;
                prevFail = true;
            } else {
                isRunning = false;
            }
        }
    }
}"""

def select_files_with_all_extensions(dir, extensions, include_subdirectories=True):
    matches = {}
    
    if include_subdirectories:
        for root, _, filenames in os.walk(dir):
            for filename in filenames:
                name, ext = os.path.splitext(filename)
                if ext in extensions:
                    if name not in matches:
                        matches[name] = set()
                    matches[name].add(ext)
    else:
        for filename in os.listdir(dir):
            name, ext = os.path.splitext(filename)
            if ext in extensions:
                if name not in matches:
                    matches[name] = set()
                matches[name].add(ext)
    
    result = [os.path.join(dir, name) for name, exts in matches.items() if exts == set(extensions)]
    return result

# def run(cmd): 
#     return subprocess.check_output(cmd.split(" ")).decode(sys.stdout.encoding)

def run(cmd): 
    completed_process = subprocess.run(cmd.split(" "), capture_output=True, text=True)

    return_code = completed_process.returncode
    stdout = completed_process.stdout
    stderr = completed_process.stderr

    return return_code, stdout, stderr

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


def rm_exstension(files):
    return ["".join(f.split(".")[:-1]) for f in files]

def gen(f):
    program = open(f"{f}.cpp", 'r').read()
    split_on_main = re.split('(?:void|int)\smain[^{]*{', program)
    main_function = split_on_main[-1]
    print(main_function)

    split_end_main = main_function.split("}")
    main_body = "}".join(split_end_main[:-1]).replace("\n", "")
    # TODO better

    lines = main_body.split(";")[:-1]
    # lines = [l.replace("(",/ "").replace(")", "") for l in lines]
    num_to_str = {str(k+1): v for k, v in enumerate(lines)}
    # print(lines)
    # print(num_to_str)
    new_stms = [f"try {{ std::cout << \"{num}:\" << {num_to_str[num].strip()} <<std::endl; }} catch (const std::exception& e) {{ std::cout << \"{num}\" << \"fail\" <<std::endl;}}" for num in super_permutations[len(lines)]]
    for i in range(0, len(new_stms)-1, len(lines)):
        new_stms[i] = f"std::cout << \"block:{int(i/5)}\\n\";\n" + new_stms[i]
    new = ";\n".join(new_stms)
    


    # rebuild the program
    permutations_program = """#include <iostream>
#include <exception>
#include <functional>\n"""+ split_on_main[0] + "" + re.findall(r'(?:void|int)\smain[^{]*{', program)[0] + new + split_end_main[-1] + ";"+ "return 0;" + "}"
    path, filename = os.path.dirname(f), os.path.basename(f)
    
    # print(permutations_program)
    # print(path, filename)
    # print(re.findall(r"(?:void|int)\smain[^{]*{", program))
    open(os.path.join(os.path.join(path, "permutations"), f"permutations_{filename}.cpp"), 'w+').write(permutations_program)

    # # n_functions = \b(void|int)\b f[0-9]
    # lines = program.split("\n")
    # n_calls = len([l for l in lines if not re.search(r"f[0-9]+_", l) and not re.search(r"(void|int)", l)])
    # print(n_calls)
if __name__ == "__main__":
    DIR = 'chop'
    # run(f"rm -r {DIR}/target")
    run(f"mkdir -p {DIR}/permutations")
    # run(f"for file in {DIR}/*.cpp; do cp {DIR}/run/'$file'; done")

    files = select_files_with_all_extensions(f"{DIR}", ['.cpp'], include_subdirectories=False)
    for f in files:
        gen(f)

    
    # for f in glob.glob(os.path.join(DIR, "permutations_*.cpp")):
    #     os.remove(f)
    # # 
    # try:
    #     print(run(f"bash regen-funcons.sh {DIR}"))
    # except:
    #     pass

