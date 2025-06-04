import os.path
import subprocess

def run_python_file(working_directory, file_path):
    allowed_root = os.path.abspath(working_directory) # absolute path to allowed directory root
    target_path = os.path.abspath(os.path.join(working_directory, file_path)) #full, combined path of target directory
    is_safe = target_path.startswith(allowed_root) # true if target directory is within scope of working directory


    if not is_safe:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(target_path): # believe this is right, possibly file_path
        return f'Error: File "{file_path}" not found.'
    
    if not target_path.endswith('.py'): # might not be right
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        result = subprocess.run(['python3', target_path],
                                timeout=30,
                                stderr=subprocess.PIPE,
                                stdout=subprocess.PIPE,
                                cwd=working_directory)

    except Exception as e:
        return f"Error: executing Python file: {e}"

    return_string = ""

    out_output = str(result.stdout)
    err_output = str(result.stderr)

    if out_output == "":
        if err_output == "":
            return_string += "No output produced\n"
        else:
            return_string += f"STDERR:{err_output}\n"
    else:
        return_string += f"STDOUT:{out_output}\n"
        if err_output != "":
            return_string += f"STDERR:{err_output}\n"
    
    if result.returncode != 0:
       return_string += f"Process exited with code {result.returncode}\n"

    return return_string