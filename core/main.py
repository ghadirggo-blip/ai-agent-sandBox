import argparse
import os #library that read from ubuntu 
from dotenv import load_dotenv #bring load_dotenv from libraty dotenv
from core.prompts import system_prompt
from openai import OpenAI
from functions.available_func import available_functions
import json
from functions.call_function import call_function

#1
load_dotenv() #this bring all variable form env and put it in
            ##Environment Variables ram for ex           
api_key = os.environ.get("OPENROUTER_API_KEY")
model_name=os.environ.get("MODEL")

if api_key is None:
    raise RuntimeError("OPENROUTER_API_KEY is missing from the .env file!")


#3
client = OpenAI(
    base_url="https://openrouter.ai/api/v1", # the trick we point the url to Open router
    api_key=api_key,
)

def run_agent_loop(user_prompt: str, verbose: bool = False) -> str:
 #4 array of messages
 messages = [
    {"role": "system", "content": system_prompt},          #ai read message in orders
    {"role": "user", "content": user_prompt},
 ]
# 1
 for _ in range(20):
    response = client.chat.completions.create(
        model=model_name,
        messages=messages,
        temperature=0,  # remove all addition from ai
        tools=available_functions,
    )
    
    if response.usage is None:
        raise RuntimeError("Api response usage data is missing!") #make sure data of tokens are sent

    # contain result, number of token
    if verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")

    message = response.choices[0].message
    # the message returns the first response or calling a tool, from ai

    #check calling tool
    if message.tool_calls:
        messages.append(message)
        
        for tool_call in message.tool_calls:
            # Call the dispatcher function we built
            result_message = call_function(tool_call, verbose=verbose)
            
            # Ensure the content is not empty
            if not result_message.get("content"):
                raise Exception(f"Tool call {tool_call.function.name} returned empty content.")
                
            messages.append(result_message)
            if verbose:
                print(f"-> {result_message['content']}")
        
        # بعد انتهاء الـ for loop للأدوات، الـ while/for الرئيسية ستعيد طلب الـ API تلقائياً بالنتائج الجديدة

    else:
        # Return regular text response if no tool was called
        return message.content

 else:
    return "Error: Maximum iterations reached without a final response."
 
if __name__ == "__main__": # run in ubuntu
 
 parser = argparse.ArgumentParser(description="Chatbot")
 parser.add_argument("user_prompt", type=str, help="User prompt:") # will wait until u write
 parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
 args = parser.parse_args() #save the prompt in parser.parse_args() and scan all phrase searsh for --verboose
 #if incluse will put action=true else action = false
 # Now we can access `args.user_prompt`

 final_response = run_agent_loop(args.user_prompt, verbose=args.verbose)
 print("Response:")
 print(final_response)
