import os.path

def overwrite_file(working_directory, file_path, content):

    allowed_root = os.path.abspath(working_directory) # absolute path to allowed directory root
    target = os.path.abspath(os.path.join(working_directory, file_path)) #full, combined path of target directory
    is_safe = target.startswith(allowed_root) # true if target directory is within scope of working directory

    if not is_safe:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    

    
    try:
        exists = os.path.exists(os.path.dirname(target)) # true if path to file already exists
 
        if not exists:
            os.makedirs(os.path.dirname(target))

        with open(target, "w") as f:
            f.write(content)
            
        return f'Successfully wrote to "{file_path}" ({len(content)} bytes written)'
    
    except Exception as e:
        return f'Error: {e}'

    