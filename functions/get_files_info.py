import os.path

def get_files_info(working_directory, directory=None):

    allowed_root = os.path.abspath(working_directory) # absolute path to allowed directory root
    target_path = os.path.abspath(os.path.join(working_directory, directory)) #full, combined path of target directory
    is_safe = target_path.startswith(allowed_root) # true if target directory is within scope of working directory


    if not is_safe:
        return f'Error: Cannot list "{target_path}" as it is outside the permitted working directory'
    if not os.path.isdir(target_path):
        return f'Error: "{target_path}" is not a directory'
    
    #Build and return a string representing the contents of the directory. It should use this format:
    """
    - README.md: file_size=1032 bytes, is_dir=False
    - src: file_size=0 bytes, is_dir=True
    - package.json: file_size=1234 bytes, is_dir=False
    """
    try:
        contents = os.listdir(target_path)
        full_dir_contents = [] # to hold all the strings of file info
        

        for file_name in contents:
            full_path_name = os.path.join(target_path,file_name)

            is_dir = os.path.isdir(full_path_name)

            if is_dir:
                file_size = 0
            else:
                file_size = os.path.getsize(full_path_name)

            full_dir_contents.append(f"- {file_name}: file_size={file_size} bytes, is_dir={is_dir}")
        return '\n'.join(full_dir_contents)
    
    except Exception as e:
        return f'Error: {e}'
    

    