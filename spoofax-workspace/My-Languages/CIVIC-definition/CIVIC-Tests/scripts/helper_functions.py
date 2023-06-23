import subprocess
import os
import shlex
import pathlib
import logging
import re
def run(cmd): 
    completed_process = subprocess.run(cmd, capture_output=True, text=True, shell=True)

    return_code = completed_process.returncode
    stdout = completed_process.stdout
    stderr = completed_process.stderr

    return return_code, stdout, stderr


def select_files_with_extensions(dir, extensions, include_subdirectories=True):
    matches = {}
    
    if include_subdirectories:
        for root, _, filenames in os.walk(dir):
            for filename in filenames:
                for extension in extensions:
                    if filename.endswith(extension):
                        basename = filename[:filename.rfind(extension)]
                        if basename not in matches:
                            matches[basename] = set()
                        matches[basename].add(extension)
    else:
        for filename in os.listdir(dir):
            for extension in extensions:
                if filename.endswith(extension):
                    basename = filename[:filename.rfind(extension)]
                    if basename not in matches:
                        matches[basename] = set()
                    matches[basename].add(extension)

    result = [os.path.join(dir, name) for name, exts in matches.items() if exts == set(extensions)]
    return result

def get_logger(name, log_file, level=logging.INFO):
    """Create a logger object"""
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

    handler = logging.FileHandler(log_file)        
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger


def create_civ_file(file):
    
    with open(file + ".cpp", "r") as cpp_file:
        cpp_code = cpp_file.read()
        cpp_code = cpp_code.replace("#", "")
    
    with open(file + ".civ", "w") as civ_file:
        civ_file.write(cpp_code)

def run_with_log(cmd, str, logger):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

    # Remove ANSI escape codes from stdout and stderr
    stdout = re.sub(r'\x1b\[[0-9;]*[mK]', '', result.stdout)
    stderr = re.sub(r'\x1b\[[0-9;]*[mK]', '', result.stderr)

    logger.info(f"{str} {result.returncode}, {stdout}, {stderr}")
