import argparse
from helper_functions import run,select_files_with_extensions, get_logger, create_civ_file, run_with_log
import random
import datetime
import os
import subprocess
import threading
import re
import traceback
def create_cpp_output(directory, f, logger): 
    try:
        print("ffsgsg")
        logger.info(f"Creating cpp for: {f}")
        out_file = f + "_cpp.output"
        if os.path.exists(out_file):
            return
        # with open(out_file, 'a') as file:file.write("")
        container_name = f"cpp_container_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}_{random.randint(1000, 9999)}"
        run_with_log(f"docker run --name {container_name} -v {os.path.abspath(directory)}:/usr/src/myapp -td test_cpp_image:latest", "Created container", logger)

        command = f"g++ -std=c++2b -O0 -o output /usr/src/myapp/{os.path.basename(f+'.cpp')}"
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
            thread.join(timeout=30)
            if thread.is_alive():
                raise subprocess.TimeoutExpired(process.args, timeout=15, output=''.join(output))
            
            return_code = process.wait()
            output = ''.join(output).strip()
            with open(out_file, 'w') as file:
                file.write(output)
            logger.info(f"Succes, {output}")

        except subprocess.TimeoutExpired:
            print(f"out:{output}")
            logger.info("Timeout")
            run_with_log(f"docker exec -it {container_name} /bin/bash -c 'pkill -f ./output'", "Terminating ./output", logger)

            output = ''.join(output).strip()
            with open(out_file, 'w') as file:
                file.write(output+"timeout")
            logger.info(f"Wrote partial result {output}")
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        logger.error(traceback.format_exc())
    

def main():
    parser = argparse.ArgumentParser(description='Process some directories.')
    parser.add_argument('regen', help='path to regen.sh')
    parser.add_argument('dockerfile_dir', type=str, help='Dir with a Dockerfile')
    parser.add_argument('directories', metavar='DIR', nargs='+', help='input directories')
    args = parser.parse_args()
    
    # print(run(f"docker build -t test_cpp_image:latest -f Dockerfile {os.path.abspath(args.dockerfile_dir)}"))

    # Access the directories as a list
    directory_list = args.directories

    # Process the directories as needed
    for directory in directory_list:
        print('Processing directory:', directory)

        files = select_files_with_extensions(directory, [".cpp"], include_subdirectories=False)
      
        cpp_log_file = os.path.join(directory, "cpp_debug_file")
        with open(cpp_log_file, 'w') as file:file.truncate(0)
        cpp_logger = get_logger("cpp_logger", cpp_log_file)
        cpp_logger.info("Started")

        # for f in files:
        #     create_cpp_output(directory, f, cpp_logger)
        for handler in cpp_logger.handlers:
            handler.close()
            cpp_logger.removeFilter(handler)
        for f in files:
            create_civ_file(f)
        run(f"bash {args.regen} {directory}")
        files = select_files_with_extensions(directory, [".cpp", ".civ", ".fct"], include_subdirectories=False)

        # for f in files:

        # create_fct_output(files)

if __name__ == '__main__':
    main()