import subprocess
import os
import shlex
import pathlib
def run(cmd): 
    completed_process = subprocess.run(cmd.split(" "), capture_output=True, text=True)

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
    if len(matches.keys()) == 0:
        return []
    result = [os.path.join(dir, name) for name, exts in matches.items() if exts == set(extensions)]
    return result

