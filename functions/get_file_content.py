import os.path

def get_file_content(working_directory, file_path):
    MAX_CHARS = 10000 # limit to file contents listing

    allowed_root = os.path.abspath(working_directory) # absolute path to allowed directory root
    target = os.path.abspath(os.path.join(working_directory, file_path)) #full, combined path of target directory
    is_safe = target.startswith(allowed_root) # true if target directory is within scope of working directory


    if not is_safe:
        return f'Error: Cannot read "{target}" as it is outside the permitted working directory'
    if not os.path.isfile(target):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(target, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            over_limit_character = f.read(1)
                
            if over_limit_character != "":
                file_content_string += '\n[...File "{file_path}" truncated at 10000 characters]'

        return file_content_string    
         
    except Exception as e:
        return f'Error: {e}'

   

