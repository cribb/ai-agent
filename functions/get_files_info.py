import os
from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)


def get_files_info(working_directory, directory="."):

    # print(f"Working directory: {working_directory}")
    # print(f"subdirectory: {directory}")

    workpath = os.path.abspath(working_directory)
    subpath = os.path.abspath(os.path.join(workpath, directory))
    
    # print(f"Working path: {workpath}")
    # print(f'Checking path: {subpath}')

    in_bounds = subpath.startswith(workpath)

    if not in_bounds:
        err_str = f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        print(err_str)
        return err_str

    if not os.path.isdir(subpath):
        err_str = f'Error: "{directory}" is not a directory'
        print(err_str)
        return err_str
    
    filelist = os.listdir(path=subpath)

    # Tailor the output to match what's in boot.dev's spec...
    if subpath == workpath:
        print(f"Result for current directory:")
    else:
        print(f"Result for '{directory}' directory:")
    
    # Iterate through files and report as per spec...
    for file in filelist:

        # print(f" --> File: {file}")

        filename = os.path.abspath(os.path.join(subpath,file))
        # print(f" --> Filename: {filename}")

        is_dir = os.path.isdir(filename)
        # print(f" --> is_dir: {is_dir}")

        filesize = os.path.getsize(filename)
        # print(f" --> filesize: {filesize}")

        print(f"- {file}: file_size={filesize} bytes, is_dir={is_dir}")
    
