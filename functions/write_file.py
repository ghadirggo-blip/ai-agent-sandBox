import os
def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        working_directory_path=os.path.abspath(working_directory)
        target_path=os.path.normpath(os.path.join(working_directory_path,file_path))

        valid_path=os.path.commonpath([working_directory_path,target_path])==working_directory_path

        if not valid_path:
           return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if  os.path.isdir(target_path):
           return  f'Error: Cannot write to "{file_path}" as it is a directory'

        # Ensure all necessary parent directories exist
        parent_dir = os.path.dirname(target_path)
        os.makedirs(parent_dir, exist_ok=True)
        #write in the file
        with open(target_path,"w",encoding="utf-8") as f:
            file_content=f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"error:{e}"