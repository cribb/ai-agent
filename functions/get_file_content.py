import os

MAX_CHARS = 10000

def get_file_content(working_directory, file_path):
    
    workpath = os.path.abspath(working_directory)
    filename = os.path.abspath(os.path.join(workpath, file_path))
    
    # print(f"Working path: {workpath}")
    # print(f'Checking file: {filename}')

    in_bounds = filename.startswith(workpath)
    if not in_bounds:
        err_str = f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        return err_str

    is_file = os.path.isfile(filename)    
    if not is_file:
        err_str = f'Error: File not found or is not a regular file: "{file_path}"'
        return err_str

    with open(filename, "r") as f:
        file_content = f.read(MAX_CHARS)

    if len(file_content) >= MAX_CHARS:
        file_content += f' [...File "{file_path}" truncated at {MAX_CHARS} characters].'

    return file_content
