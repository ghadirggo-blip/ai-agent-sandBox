schema_write_file_info = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes text content to a specified file relative to the working directory, creating parent directories if they don't exist",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file to write to, relative to the working directory",
                },
                "content": {
                    "type": "string",
                    "description": "The text content to write into the file",
                },
            },
            "required": ["file_path", "content"],
        },
    },
}