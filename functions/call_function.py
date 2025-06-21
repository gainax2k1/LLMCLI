import os.path
import subprocess
from google.genai import types
from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.overwrite_file import overwrite_file
from functions.run_python_file import run_python_file


def call_function(function_call_part, verbose=False):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    working_directory = './calculator'

    function_call_part.args["working_directory"] = working_directory

    function_map = {
        "get_file_content": get_file_content,
        "get_files_info": get_files_info,
        "overwrite_file": overwrite_file,
        "run_python_file": run_python_file
    } 
    
    try:
        result_val = function_map[function_call_part.name](**function_call_part.args)
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"result": result_val},
                )
            ],
        )

    except:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"error": f"Unknown function: {function_call_part.name}"},
                )
            ],
        )
