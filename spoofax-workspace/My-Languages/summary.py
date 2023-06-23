import subprocess
import re

output = subprocess.check_output("find . -type f -iname '*cpp*.cbs' -not -type l", shell=True)
output = output.decode('utf-8')

file_paths = output.split('\n')

import subprocess
import re

output = subprocess.check_output("find . -type f -iname '*cpp*.cbs' -not -type l", shell=True)
output = output.decode('utf-8')

file_paths = output.split('\n')

def parse_file_content(file_content):
    file_content = re.sub(r'\\\\.*?\n', '', file_content)
    result = []
    split_content = file_content.split('simple-class(')

    for section in split_content[1:]:
        class_pattern = re.compile(r'"([^"]*)"')
        function_pattern = re.compile(r'"([^"]*)"\s*\|\-\> method')
        class_name = class_pattern.search(section).group(1)
        
        # Find all function names
        function_matches = function_pattern.findall(section)
        current_class_functions = [match for match in function_matches]

        result.append((class_name, current_class_functions))

    return result
print("The following classes and member functions are defined:")
for file_path in file_paths:
    if file_path.strip() != '':
        with open(file_path, 'r') as file:
            file_contents = file.read()
            class_and_functions = parse_file_content(file_contents)
            for class_name, function_list in class_and_functions:
                print(f'Class Name: {class_name}\nFunctions: {", ".join(function_list)}')
                print()
