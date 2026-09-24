import os
def get_files_info(working_directory: str, directory: str = ".") -> str:
  try:
    working_directory_abs=os.path.abspath(working_directory)

    target_dir=os.path.normpath(os.path.join(working_directory_abs,directory))  

    valid_dir_target=os.path.commonpath([working_directory_abs,target_dir])==working_directory_abs

    if not valid_dir_target:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(target_dir): #make sure  target path is end by a dir AND EXISTS
            return f'Error: "{directory}" is not a directory'
    #--------------------------------
    content=os.listdir(target_dir)
  
    result_lines = []
        
    for item in content:
            item_path = os.path.join(target_dir, item)
            file_size = os.path.getsize(item_path) #this func takes PATH as param
            is_dir = os.path.isdir(item_path)  #this func takes PATH as param
            result_lines.append(f"- {item}: file_size={file_size} bytes, is_dir={is_dir}")
            
    return "\n".join(result_lines)
    
  except Exception as e:
      return f"error {e}"
      