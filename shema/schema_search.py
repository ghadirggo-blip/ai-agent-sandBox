schema_search_in_files = {
    "type": "function",
    "function": {
        "name": "search_in_files",
        "description": "Search for a specific text, keyword, or pattern across all text files in the project workspace efficiently.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The text, keyword, or code snippet to search for inside the project files",
                },
                "working_directory": {
                    "type": "string",
                    "description": "The root directory to scan (defaults to current directory if omitted)",
                },
            },
            "required": ["query"],
        },
    },
}