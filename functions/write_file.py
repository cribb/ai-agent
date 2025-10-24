import os

def write_file(working_directory, file_path, content):
    
    workpath = os.path.abspath(working_directory)
    filename = os.path.abspath(os.path.join(workpath, file_path))
    
    # print(f"Working path: {workpath}")
    # print(f'Checking file: {filename}')

    in_bounds = filename.startswith(workpath)
    if not in_bounds:
        err_str = f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        return err_str
    
    dirname = os.path.dirname(filename)
    # print(f"dirname: {dirname}")

    if not os.path.exists(dirname):
        err_str = f"Error: Path does not exist. Creating path..."
        print(err_str)
        os.mkdir(dirname)
    
    with open(filename, "w") as f:
        f.write(content)

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
