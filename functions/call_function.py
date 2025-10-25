import os
import sys
import subprocess
from google.genai import types

from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python_file import run_python_file
from functions.write_file import write_file


def call_function(function_call_part, verbose=False):
    
    func_name = function_call_part.name
    func_args = function_call_part.args

    if verbose:
        print(f"Calling function: {func_name}({func_args})")
    else:
        print(f" - Calling function: {func_name}")

    function_dict = {"get_file_content": get_file_content,
                     "get_files_info": get_files_info, 
                     "run_python_file": run_python_file,
                     "write_file": write_file}
    
    if func_name not in function_dict:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=func_name,
                    response={"error": f"Unknown function: {func_name}"},
                )
            ],
        )
    
    # Add our hardcoded "working_directory" argument       
    func_args["working_directory"] = "./calculator"

    # THIS IS THE MEAT RIGHT HERE
    function_result = function_dict[func_name](**func_args)

    # Return the type.content if successful
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=func_name,
                response={"result": function_result},
            )
        ],
    )
