import os
MAX_CHARS=10000
def get_file_content(working_directory: str, file_path: str) -> str:
 try:
    working_directory_path=os.path.abspath(working_directory)

    target_file_path=os.path.normpath(os.path.join(working_directory_path,file_path))

    valid_dir_file=os.path.commonpath([working_directory_path,target_file_path])==working_directory_path

    if not valid_dir_file:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_file_path):
       return f'Error: File not found or is not a regular file: "{file_path}"'


# read the file
#stored Max char in config file

    with open(target_file_path, "r",encoding="utf-8") as f:
      file_content_string = f.read(MAX_CHARS)
      if f.read(1):
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
    return file_content_string
 except Exception as e:
      return f"error {e}"