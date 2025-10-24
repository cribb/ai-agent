import os
import sys
import subprocess

AITIMEOUT = 3

def run_python_file(working_directory, file_path, args=[]):
    workpath = os.path.abspath(working_directory)
    filename = os.path.abspath(os.path.join(workpath, file_path))
    
    # print(f"Working path: {workpath}")
    # print(f'Checking file: {filename}')

    in_bounds = filename.startswith(workpath)
    if not in_bounds:
        err_str = f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        return err_str

    is_file = os.path.isfile(filename)    
    if not is_file:
        err_str = f'Error: File "{file_path}" not found.'
        return err_str

    if not filename.endswith(".py"):
        err_str = f'Error: "{file_path}" is not a Python file.'
        return err_str
    
    # if len(args) == 0:
    #     return "No process is defined in the arguments provided to subprocess"
    
    cmd = [sys.executable, filename, *args]
    # print(f"cmd= {cmd}")
    try: 
        process_output = subprocess.run(cmd, cwd=workpath, capture_output=True, timeout=AITIMEOUT)
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
    stdo = process_output.stdout.decode("utf-8")
    stde = process_output.stderr.decode("utf-8")

    if len(stdo) == 0:
        return "No output produced."
    
    output = ''
    output += f"STDOUT: {stdo}"
    output += f"STDERR: {stde}"

    exit_code = process_output.returncode
    if not exit_code == 0:
        output += f"Process exited with code {exit_code}"

    return output
