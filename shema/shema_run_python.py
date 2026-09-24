schema_run_python_file_info = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Execute a Python script file directly. Use this tool IMMEDIATELY when the user asks to run a python file or test file, without calling get_files_info first",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the Python file to execute, relative to the working directory",
                },
                "args": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "Optional list of string arguments to pass to the Python script",
                },
            },
            "required": ["file_path"],
        },
    },
}