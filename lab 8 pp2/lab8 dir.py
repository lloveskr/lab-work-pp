import os

def list_directories_files(path):
    dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    all_content = [content for content in os.listdir(path)]
    return dirs, files, all_content

specified_path = '/path/to/your/directory'
directories, files, all_content = list_directories_files(specified_path)
print("Directories:", directories)
print("Files:", files)
print("All Directories/Files:", all_content)



import os

def check_access(path):
    exists = os.path.exists(path)
    readable = os.access(path, os.R_OK)
    writable = os.access(path, os.W_OK)
    executable = os.access(path, os.X_OK)
    return exists, readable, writable, executable

specified_path = '/path/to/your/directory_or_file'
access_info = check_access(specified_path)
print("Existence, Readability, Writability, Executability:", access_info)


import os

def check_access(path):
    exists = os.path.exists(path)
    readable = os.access(path, os.R_OK)
    writable = os.access(path, os.W_OK)
    executable = os.access(path, os.X_OK)
    return exists, readable, writable, executable

specified_path = '/path/to/your/directory_or_file'
access_info = check_access(specified_path)
print("Existence, Readability, Writability, Executability:", access_info)


import os

def path_info(path):
    exists = os.path.exists(path)
    if exists:
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        return exists, filename, directory
    else:
        return exists, None, None

given_path = '/path/to/your/file_or_directory'
path_existence, filename, directory = path_info(given_path)
print("Path Exists:", path_existence)
if path_existence:
    print("Filename:", filename)
    print("Directory:", directory)


def count_lines(file_path):
    with open(file_path, 'r') as file:
        line_count = sum(1 for line in file)
    return line_count

text_file_path = 'path/to/your/text_file.txt'
lines_count = count_lines(text_file_path)
print("Number of lines in the file:", lines_count)


