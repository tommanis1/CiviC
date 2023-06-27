import argparse
from helper_functions import run,select_files_with_extensions, get_logger, create_civ_file, run_with_log
import random
import datetime
import os
import subprocess
import threading
import re
import concurrent.futures
import traceback
import json
GPP_FLAGS = "-std=c++2b -O0"
TIMEOUT = 30
ITERATIONS = 1
CONFIG = "--non-deterministic value-operations"

def create_cpp_output(directory, f):
    logger = get_logger(f"cpp_logger_{os.path.basename(f)}", f+"_cpp.debug")
    try:
        ret = []

        logger.info(f"Creating cpp for: {f}")
        # out_file = f + "_cpp.output"
        # if os.path.exists(out_file):
        #     return
        # with open(out_file, 'a') as file:file.write("")
        container_name = f"cpp_container_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}_{random.randint(1000, 9999)}"
        run_with_log(f"docker run --name {container_name} -v {os.path.abspath(directory)}:/usr/src/myapp -td test_cpp_image:latest", "Created container", logger)

        for i in range(ITERATIONS):
            logger.info(f"it {i}")
            command = f"g++ {GPP_FLAGS} -o output /usr/src/myapp/{os.path.basename(f+'.cpp')}"
            run_with_log(f"docker exec -it {container_name} /bin/bash -c '{command}'", "Compile", logger)

            # Run the command in a subprocess
            process = subprocess.Popen(
                ["docker", "exec", "-it", container_name, "/bin/bash", "-c", "./output"],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
            )
            logger.info("Started running")
            output = []
            def target(process, output):
                for line in iter(process.stdout.readline, ''):
                    output.append(line)
            thread = threading.Thread(target=target, args=(process, output))
            thread.start()

            try:
                thread.join(timeout=TIMEOUT)
                if thread.is_alive():
                    raise subprocess.TimeoutExpired(process.args, timeout=TIMEOUT, output=''.join(output))
                
                return_code = process.wait()
                output = ''.join(output).strip()
                ret.append(output)
                # with open(out_file, 'a') as file:
                #     file.write(output)
                logger.info(f"Succes, {output}")

            except subprocess.TimeoutExpired:
                print(f"out:{output}")
                logger.info("Timeout")
                run_with_log(f"docker exec -it {container_name} /bin/bash -c 'pkill -f ./output'", "Terminating ./output", logger)

                output = ''.join(output).strip()
                ret.append(output+"timeout")

                logger.info(f"Wrote partial result {output}")
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        logger.error(traceback.format_exc())
    for handler in logger.handlers:
        handler.close()
        logger.removeFilter(handler)
    
    return ret
def create_fct_output(directory, f, rfct): 
    logger = get_logger(f"fct_logger_{os.path.basename(f)}", f+"_fct.debug")

    ret = []
    for i in range(ITERATIONS):

        seed = random.randint(0, 65535)
        code, stdout, stderr = run(f'ulimit -Sv 4000000 && {rfct} --show-output-only true --refocus false {CONFIG} --seed {seed} {f + ".fct"}')

                    # print(code, stdout, stderr)
        stdout = "".join(stdout)
        program_return = stdout.split("Result:\n")[-1].split("\n")[0]
        program_stdout = stdout.split("Output Entity: standard-out\n")[-1].split("\n")[0]
        logger.info(f"{code}{stdout}{stderr}")           
        o_string = "".join(re.findall(r'("[^"]*"|[^,]+)', program_stdout)).replace("[]","").replace('"', '').replace("\\n", "\n")
        ret.append(o_string)
    for handler in logger.handlers:
        handler.close()
        logger.removeFilter(handler)
    return ret


def main():
    parser = argparse.ArgumentParser(description='Process some directories.')
    parser.add_argument('regen', help='path to regen.sh')
    parser.add_argument('dockerfile_dir', type=str, help='Dir with a Dockerfile')
    parser.add_argument('data_folder', help='Path for summary output')
    parser.add_argument('rfct', help='Runfct')

    parser.add_argument('directories', metavar='DIR', nargs='+', help='input directories')

    parser.add_argument('-t', '--threads', type=int, default=4, help='Number of threads to use')
    args = parser.parse_args()
    print(run(f"docker build -t test_cpp_image:latest -f Dockerfile {os.path.abspath(args.dockerfile_dir)}"))
    directory_list = args.directories
    n_tests = 0
    n_test_syntax = 0
    n_discared = 0
    n_from_gcc = 0
    n_from_gcc_syntax = 0

    # Create a ThreadPoolExecutor
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.threads) as executor:
        # Process the directories as needed
        for directory in directory_list:
            print('Processing directory:', directory)

            files = select_files_with_extensions(directory, [".cpp"], include_subdirectories=False)
            n_tests += len(files)

            # Create a list to hold our future results
            futures = []

            # Submit tasks to thread pool
            for f in files:
                futures.append(executor.submit(process_file, directory, f, args.regen, args.rfct))

            # Wait for all tasks to complete
            concurrent.futures.wait(futures)

            data = []
            for future in futures:
                f, cpp_outputs, fct_outputs = future.result()
                test_data = {
                    "cpp_outputs": cpp_outputs,
                    "fct_outputs": fct_outputs
                }
                with open(f"{f}.json", "w") as file:
                    json.dump(test_data, file)
                data.append((f, (cpp_outputs, fct_outputs)))

            determ = [f for (f, (cpp, fct)) in data if all(val == cpp[0] for val in cpp) and all(val == fct[0] for val in fct)]
            possible_non_determ = [f for (f, (cpp, fct)) in data if all(val == cpp[0] for val in cpp) and not all(val == fct[0] for val in fct)]
            non_determ = [f for (f, (cpp, fct)) in data if not all(val == cpp[0] for val in cpp)]

            with open(os.path.join(directory, "summary"), "w") as file:
                file.write(f"""{directory}.In total there are {n_tests} deterministic tests, of these {n_test_syntax} have valid syntax for the C++ subset.
{non_determ} files where found to be non-deterministic. {possible_non_determ} could be possible_non_determ and {determ} are determ""")

            print(f"summary created in {args.data_folder}")

def process_file(directory, f, regen, rfct):
    create_civ_file(f)
    run(f"bash {regen} {directory}")
    cpp_outputs = create_cpp_output(directory, f)
    fct_outputs = create_fct_output(directory, f, rfct)
    return f, cpp_outputs, fct_outputs

if __name__ == '__main__':
    main()