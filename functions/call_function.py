import json
from collections.abc import Callable
#four functions
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.run_python_file import run_python_file
from functions.write_file import write_file

def call_function(tool_call, verbose: bool = False) -> dict:
    #The tool_call argument is one of the tool-call objects from message.tool_calls

    #1
    function_name = tool_call.function.name
    try:
        #args come from shema as json string and json.load transform to dictionary
        function_args = json.loads(tool_call.function.arguments or "{}")
    except json.JSONDecodeError:
        function_args = {}


    #2 check if verboose
    if verbose:
     print(f" - Calling function: {function_name}({function_args})")
    else:
       print(f" - Calling function: {function_name}")
 
 
    function_map: dict[str, Callable[..., str]] = {
        #left is the name of how ai know the name (Shema)
        #righ is the name of function
        "get_files_info": get_files_info,
        "get_file_content": get_file_content,
        "run_python_file": run_python_file,
        "write_file": write_file,
    }

    #3 if function does not exist
    if function_name not in function_map:
        return {
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": f"Error: Unknown function: {function_name}",
        }

    #4
    try:
        # let ai work only in calculator app (security reasons)
        function_args["working_directory"] = "./calculator"

        #unpack the argument wich is dictionary from:
        #write_file(**{"file_path": "test.py", "content": "hello"})
        #To
        #write_file(file_path="test.py", content="hello")

        result = function_map[function_name](**function_args)
      

        return {
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": result,
        }
    except Exception as e:
        return {
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": f"Error executing {function_name}: {e}",
        }