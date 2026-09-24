schema_get_file_content_info = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Read the exact content of a specific file. Use this ONLY when you need to read the text inside a file, not for listing directories.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "The path to the file whose content should be read, relative to the working directory",
                },
            },
            "required": ["file_path"],
        },
    },
}