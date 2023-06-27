import os
import re
import glob
import shutil
import subprocess
import traceback
import pexpect
import random
import os
import getpass
import threading
from datetime import datetime
import signal
import sys
from helper_functions import select_files_with_extensions, run
import argparse
import datetime
import concurrent.futures
import logging

CONFIG = "--non-deterministic value-operations"
super_permutations = [
    "0",
    "1",
    "121",
    "123121321",
    "123412314231243121342132413214321",
    "123451234152341253412354123145231425314235142315423124531243512431524312543121345213425134215342135421324513241532413524132541321453214352143251432154321",
    "123456123451623451263451236451234651234156234152634152364152346152341652341256341253641253461253416253412653412356412354612354162354126354123654123145623145263145236145231645231465231425631425361425316425314625314265314235614235164235146235142635142365142315642315462315426315423615423165423124563124536124531624531264531246531243561243516243512643512463512436512431562431526431524631524361524316524312564312546312543612543162543126543121345621345261345216345213645213465213425613425163425136425134625134265134215634215364215346215342615342165342135642135462135426135421635421365421324561324516324513624513264513246513241563241536241532641532461532416532413562413526413524613524163524136524132564132546132541632541362541326541321456321453621453261453216453214653214356214352614352164352146352143652143256143251643251463251436251432651432156432154632154362154326154321654321"
]

def block_print_stmt(block):
    return f"std::cout << \"block:{block}\\n\";\n" 

def create_permutation_file(f, permutations):
    program = open(f"{f}.cpp", 'r').read()
    split_on_main = re.split('(?:void|int)\smain[^{]*{', program)
    main_function = split_on_main[-1]

    split_end_main = main_function.split("}")
    main_body = "}".join(split_end_main[:-1]).replace("\n", "")

    lines = main_body.split(";")[:-1]

    num_to_str = {str(k+1): v for k, v in enumerate(lines)}
    count = 0
    new_stms = []
    def try_catch(c, n):
        return f"try {{ std::cout << \"count:{c} \"; {num_to_str[n].strip()} ;}}" + f" catch (...) {{ std::cout << \"fail\" <<std::endl;}}"
    for num in super_permutations[len(lines)]:
        new_stms.append(try_catch(count, num ))
        new_stms.append(try_catch(count+1, num ))
        count+=2

        
    # new_stms = [
    #     f"try {{ std::cout << \"function-call {num}:\" << {num_to_str[num].strip()} <<std::endl; }}"
    #     f" catch (const std::exception& e) {{ std::cout << \"{num}\" << \"fail\" <<std::endl;}}"
    #     for num in super_permutations[len(lines)]
    # ]
    # for i in range(0, len(new_stms)-1, len(lines)):
    #     new_stms[i] = block_print_stmt(int(i/len(lines))) + new_stms[i]
    new = ";\n".join(new_stms)

    permutations_program = (
        """#include <iostream>\n"""
        + split_on_main[0]
        + re.findall(r'(?:void|int)\smain[^{]*{', program)[0]
        + "\n"
        + new
        + split_end_main[-1]
        + ";\n"
        + "return 0;"
        + "}"
    )
    path, filename = os.path.dirname(f), os.path.basename(f)

    # os.makedirs(os.path.join(path, "permutations"), exist_ok=True)
    open(os.path.join(os.path.join(permutations), f"permutations_{filename}.cpp"), 'w+').write(permutations_program)

# def select_body(text):

#     split_on_main = re.split('(?:void|int)\smain[^{]*{', text)
#     main_function = split_on_main[-1]

#     split_end_main = main_function.split("}")
#     main_body = "}".join(split_end_main[:-1])
#     return main_body
def select_id(line):
    return line.split("function-call")[-1].split(":")[0].strip()
def generate_a_continue_file(f, count, continue_counter, logger):    
    program = open(f, 'r').read()
    split_on_main = re.split('(?:void|int)\smain[^{]*{', program)
    main_function = split_on_main[-1]

    split_end_main = main_function.split("}")
    main_body = "}".join(split_end_main[:-1])

    # logging.info(f"body: {body}")

    stmts = main_body.split(";\n")
    loc = None

    # block_stmt = block_print_stmt(block).strip().split(";")[0]
    # id_stmt = f'try {{ std::cout << "function-call {line_id}:"'
    logger.info(f"generate_a_continue_file file: {f} continue_counter:{continue_counter}, count:{count}")

    for i,stmt in enumerate(stmts):
        # logging.info(f"stmt : {stmt} ")
        if f"count:{count}" in stmt:
            loc = i
            logger.info(f"found in: {stmt}")
            break  
            
    logger.info(f"loc : {loc}")

    if loc is not None:  # If we found the location
        cont =  split_on_main[0] + re.findall(r'(?:void|int)\smain[^{]*{', program)[0] + "\n"  +";\n".join(stmts[loc+1:]) + "}" # Select all statements starting from the found location
        # logging.info(f"continuaticontinuationon statements: {cont}")
        continue_file = os.path.splitext(f)[0]+ f"_cont_{continue_counter}.cpp"
        logger.info(f"continue_file : {continue_file}")
        with open(continue_file, 'w') as file:
            file.write(cont)
        return continue_file
    else:
        logger.warning("Couldn't find the correct block and line. No continuation file generated.")
    logger.info(f"")

def run_with_log(cmd, str, logger):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

    # Remove ANSI escape codes from stdout and stderr
    stdout = re.sub(r'\x1b\[[0-9;]*[mK]', '', result.stdout)
    stderr = re.sub(r'\x1b\[[0-9;]*[mK]', '', result.stderr)

    logger.info(f"{str} {result.returncode}, {stdout}, {stderr}")


def get_logger(name, log_file, level=logging.INFO):
    """Create a logger object"""
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

    handler = logging.FileHandler(log_file)        
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

def run_cpp_tests(dir, iteration):
    logger = get_logger(f"cpp_{iteration}", os.path.join(dir, f"debug_cpp_{iteration}.log"))
    logger.info(f'Running C++ tests for iteration {iteration}')

    def target(process, output):
        for line in iter(process.stdout.readline, ''):
            output.append(line)

    # Create a Docker container for the run_tests invocation
    # container_name = f"cpp_container_{threading.get_ident()}"
    try:
        container_name = f"cpp_container_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}_{random.randint(1000, 9999)}"

        return_code, stdout, stderr = run(f"docker run --name {container_name} -v {os.path.abspath(dir)}:/usr/src/myapp -td test_cpp_image:latest")
        logger.info(f"Started container return code: {return_code}, {stdout }, {stderr}")
        files = [file + ".cpp" for file in select_files_with_extensions(dir, [".cpp"], include_subdirectories=False)]
        # logging.info(f"files{files}")
        for f in files:
            running_file = f
            count = 0
            continue_counter = 0
            was_last_run_a_fail = False
            out_file = os.path.splitext(f)[0] + f"_output_cpp-{iteration}.txt"        
            logger.info(f"Started: {f}, outfile: {out_file}")
            with open(out_file, 'w') as file:
                file.write("")
            while True:
                
                logger.info(f"Testing: {running_file}")

                command = f"g++ -std=c++2b -o output /usr/src/myapp/{os.path.basename(running_file)}"
                # run_with_log(f"docker exec -it {container_name} /bin/bash -c 'gcc -v'", "gcc -v", logger)

                run_with_log(f"docker exec -it {container_name} /bin/bash -c '{command}'", "Compile", logger)

                # Run the command in a subprocess
                process = subprocess.Popen(
                    ["docker", "exec", "-it", container_name, "/bin/bash", "-c", "./output"],
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
                )
                logger.info("Started running")
                output = []
                thread = threading.Thread(target=target, args=(process, output))
                thread.start()

                try:
                    thread.join(timeout=30)
                    if thread.is_alive():
                        raise subprocess.TimeoutExpired(process.args, timeout=15, output=''.join(output))
                    
                    return_code = process.wait()
                    output = ''.join(output).strip()
                    if not "terminate" in output:
                        with open(out_file, 'a') as file:
                            file.write(output)
                        logger.info(f"Succes, {output}")
                        was_last_run_a_fail = False
                    else:
                        logger.info(f"Terminated with {return_code} output:{output}")
                        try:
                            last_count_found = int(re.search(r'\d+', output.split("count:")[-1].strip()).group())
                            logger.info(f"count is {count}, last count found in output: {last_count_found}, output{output}")

                            count = max(count, last_count_found) + 1
                        except:
                            count += 1
                            logger.info("Getting the count failed iinc")
                        with open(out_file, 'a') as file:
                            file.write(f"count:{count},result:terminated\n")

                        continue_counter += 1
                        # generate_a_continue_file(f, block, id, continue_counter)
                        # running_file = None
                        # logger.info(f"generate_a_continue_file, {f}, {count}, {continue_counter}")
                        running_file = generate_a_continue_file(f, count, continue_counter, logger)
                        if running_file == None:
                            logger.warning("Failed to continue after timeout")
                            break
                        continue

                except subprocess.TimeoutExpired:
                    print(f"out:{output}")
                    logger.info("Timeout")
                    run_with_log(f"docker exec -it {container_name} /bin/bash -c 'pkill -f ./output'", "Terminating ./output", logger)

                    output = ''.join(output).strip()
                    with open(out_file, 'a') as file:
                        file.write(output)
                    logger.info(f"Wrote partial result {output}")

                    try:
                            last_count_found = int(re.search(r'\d+', output.split("count:")[-1].strip()).group())
                            logger.info(f"count is {count}, last count found in output: {last_count_found}, output{output}")

                            count = max(count, last_count_found) + 1
                    except:
                            count += 1
                            logger.info("Getting the count failed iinc")
                    process.terminate()

                        # logging.info(f"Writing output for id : {select_id(stmts[loc])} line {(stmts[loc])}")
                    with open(out_file, 'a') as file:
                        file.write(f"count:{count},result:timeout\n")

                    continue_counter += 1
                    # generate_a_continue_file(f, block, id, continue_counter)
                    # running_file = None
                    logger.info(f"generate_a_continue_file, {f}, {count}, {continue_counter}")
                    running_file = generate_a_continue_file(f, count, continue_counter, logger)
                    if running_file == None:
                        logger.warning("Failed to continue after timeout")
                        break
                        
                
                    # if not "count" in output: # base case
                    #     count +=1
                    was_last_run_a_fail = True
                    continue

                else:
                    break

        subprocess.run(["docker", "rm", container_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        run(f"docker rm {container_name}")
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        logger.error(traceback.format_exc())
    finally:
        for handler in logger.handlers:
            handler.close()
            logger.removeFilter(handler)
def run_funcons_tests(dir, iteration, regen):
    logger = get_logger(f"funcons_{iteration}", os.path.join(dir, f"debug_funcons_{iteration}.log"))
    logger.info(f'Running Funcons tests for iteration {iteration}')
    try:
        files = select_files_with_extensions(dir, [".cpp"], include_subdirectories=False)
        for f in files:
            create_civ_file(f)
        logger.info(f"Created {len(files)} civ files")

        run_with_log(f"bash {regen} {dir}", "Gen fct: ", logger)
        files = [f + ".civ" for f in select_files_with_extensions(dir, [".civ", ".fct"], include_subdirectories=False)]
        logger.info(f"Created {len(files)} fct files")
        for f in files:
            running_file = f
            count = 0
            continue_counter = 0
            was_last_run_a_fail = False
            out_file = os.path.splitext(f)[0] + f"_output-{iteration}.txt"        
            logger.info(f"Started: {f}, outfile: {out_file}")
            with open(out_file, 'w') as file:
                file.write("")
            while True:
                logger.info(f"Testing: {running_file}")

                seed = random.randint(0, 65535)
                code, stdout, stderr = run(f'ulimit -Sv 4000000 && /home/l/.cabal/bin/CIVIC-Runfct --show-output-only true --refocus false {CONFIG} --seed {seed} {os.path.splitext(running_file)[0] + ".fct"}')

                # print(code, stdout, stderr)
                stdout = "".join(stdout)
                program_return = stdout.split("Result:\n")[-1].split("\n")[0]
                program_stdout = stdout.split("Output Entity: standard-out\n")[-1].split("\n")[0]
                    
                o_string = "".join(re.findall(r'("[^"]*"|[^,]+)', program_stdout)).replace("[]","").replace('"', '').replace("\\n", "\n")
                logger.info(f"deadlock {program_return} {program_stdout}")
                if "deadlock" in program_return:
                    counts = program_stdout.split("count:")
                    count = int(re.search(r'\d+', counts[-1]).group())
                    logger.info(f"deadlock for count {count}")

                    with open(out_file, 'a') as file:
                        file.write("\n".join(o_string.split("\n")[:-1]) + "\n")
                        file.write(f"count:{count},result:timeout\n")
                    continue_counter+=1

                    continue_file = generate_a_continue_file(f, count, continue_counter, logger)
                    if continue_file == None:
                        logger.warning("Failed to continue after timeout")
                        break
                    
                    running_file = os.path.splitext(continue_file)[0]
                    create_civ_file(running_file)
                    logger.info(f"Contine civ file {running_file}")
                    run_with_log(f"bash {regen} {dir}", "Gen fct: ", logger)
                    
                    if not os.path.exists(running_file + ".fct"):
                        logger.warning(f"Failed creat fct file for {running_file}")
                        break

                    continue
                elif code != 0: # determien heter runfct failed or call to std::terminate
                    print("funcons failed", running_file)
                    logger.info(f"{running_file} failed {code} {stdout} {stderr}" )
                    numbers = re.findall(r'count:(\d+)\n$', o_string) # exculde partial lines, hopefully
                    if numbers:
                        count = max(map(int, numbers)) + 1
                    else:
                        count = 0

                    with open(out_file, 'a') as file:
                        file.write(o_string)
                        file.write(f"count:{count},result:Runfct failed\n")
                    continue_counter+=1
                    continue_file = generate_a_continue_file(f, count, continue_counter, logger)
                    if continue_file == None:
                        logger.warning("Failed to continue after Runfct fail")
                        break

                    running_file = os.path.splitext(continue_file)[0]
                    create_civ_file(running_file)
                    logger.info(f"Contine civ file {running_file}")
                    run_with_log(f"bash {regen} {dir}", "Gen fct: ", logger)
                    
                    if not os.path.exists(running_file + ".fct"):
                        logger.warning(f"Failed creat fct file for {running_file}")
                        break

                

                # print(f"out: {string}")
                    logger.info("Succes")
                    break
                else:
                    with open(out_file, 'a') as file:
                        file.write(o_string)


            # print(stdout)
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        logger.error(traceback.format_exc())
    finally:
        for handler in logger.handlers:
            handler.close()
            logger.removeFilter(handler)


def create_civ_file(file):
    
    with open(file + ".cpp", "r") as cpp_file:
        cpp_code = cpp_file.read()
        cpp_code = cpp_code.replace("#", "")
    
    with open(file + ".civ", "w") as civ_file:
        civ_file.write(cpp_code)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run multiple iterations of tests")
    parser.add_argument('data_folder', type=str, help='Data folder path')
    parser.add_argument('number_iterations', type=int, help='Number of iterations')
    parser.add_argument('thread_pool_size', type=int, help='Size of the thread pool')
    parser.add_argument('input_folder', type=str, help='Input folder path')
    parser.add_argument('dockerfile_dir', type=str, help='Dir with a Dockerfile')
    parser.add_argument('regen_funcons_script', type=str, help='regen_funcons_script')


    args = parser.parse_args()

    # Build the Docker image
    print(run(f"docker build -t test_cpp_image:latest -f Dockerfile {os.path.abspath(args.dockerfile_dir)}"))
    # return_code, stdout, stderr = subprocess.run(docker_build_cmd, shell=True, capture_output=True)



    # Prepare the target directory
    time_str = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    target = os.path.join(args.data_folder, "runs", f"run-{time_str}")
    run(f"mkdir -p {target}")

    # Prepare the permutations directory
    permutations = os.path.join(target, "permutations")
    run(f"mkdir -p {permutations}")

    # Select all .cpp files and create permutation files
    files = select_files_with_extensions(args.input_folder, [".cpp"], include_subdirectories=False)
    for f in files:
        create_permutation_file(f, permutations)

    files = [os.path.basename(f) for f in files]
    # Run tests in a separate thread for each iteration
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.thread_pool_size) as executor:
        for i in range(args.number_iterations):
            cpp_dir = os.path.join(target, f'iteration-{i}-cpp')
            run(f"mkdir -p {cpp_dir}")

            funcons_dir = os.path.join(target, f'iteration-{i}-funcons')
            run(f"mkdir -p {funcons_dir}")

            shutil.rmtree(cpp_dir, ignore_errors=True)
            shutil.copytree(permutations, cpp_dir)
            shutil.rmtree(funcons_dir, ignore_errors=True)
            shutil.copytree(permutations, funcons_dir)

            executor.submit(run_cpp_tests, cpp_dir, i)
            executor.submit(run_funcons_tests, funcons_dir, i, args.regen_funcons_script)

    # cpp_files = 
    # for each test file colect all the output files for all iterations 
    output_files = []



# with concurrent.futures.ThreadPoolExecutor(max_workers=args.thread_pool_size) as executor:
#     for i in range(args.number_iterations):
#             iteration_dir = os.path.join(target, f'iteration-{i}')
#             executor.submit(run_funcons_tests, iteration_dir, i)
#         # clean the dirs.
#         # Do the same run butwith funcons