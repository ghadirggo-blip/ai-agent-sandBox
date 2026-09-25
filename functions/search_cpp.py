import subprocess

def search_in_files(query: str, working_directory:str) -> str:
  #query is what your looking for
  #working_directory is where you start from
    try:
        
        cmd = ["grep", "-rn", "--exclude-dir={.git,__pycache__,venv,.uv}", query, working_directory]
        
       #using grep (this won't work if the user did not installed linux)
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=5)
        
        if result.stdout:
           
            return f"[SUCCESS: MATCH FOUND]\n{result.stdout}\n\n[INSTRUCTION: Stop searching immediately and answer the user.]"
        return "No matches found."
        
    except Exception as e:
        return f"Error executing search: {str(e)}"
        