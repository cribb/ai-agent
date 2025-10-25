import os
import sys
import subprocess
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs python code, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file containing python code to be ran, constrained to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.STRING,
                description="The arguments to pass to 'file_path'",
            ),
        },
    ),
)

AITIMEOUT = 30

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

    output = ''
    if len(stdo)>0:
        output += f"STDOUT: {stdo}\n"
    if len(stde)>0:
        output += f"STDERR: {stde}\n"

    # print(f"Output: {output}")

    exit_code = process_output.returncode
    if not exit_code == 0:
        output += f"Process exited with code {exit_code}"

    if len(output) == 0:
        return "No output produced."

    return output
