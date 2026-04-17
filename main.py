import os
import argparse

from dotenv import load_dotenv
from google import genai
from google.genai import types

system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

from call_function import *

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content, 
        schema_run_python_file,
        schema_write_file],
)

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)



def main():
    try:
        parser = argparse.ArgumentParser(description="Chatbot")
        parser.add_argument("user_prompt", type=str, help="User prompt")
        parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
        args = parser.parse_args()
        messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
        if api_key == None:
            raise RuntimeError("Api key not found")
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions],
                system_instruction=system_prompt))
        if response == None:
            raise RuntimeError("Failed to get response from model")

        if args.verbose == True:
            print(f"User prompt: {args.user_prompt}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        print(response.text)
     
        # function_results = []
        if response.function_calls is None:
            return
        for function_call in response.function_calls:
        #    print(f"Calling function: {function_call.name}({function_call.args})")
            function_call_result = call_function(function_call, verbose=args.verbose)
            if function_call_result.parts == None:
                raise Exception("Empty parts")
            if function_call_result.parts[0].function_response == None:
                raise Exception("Empty function response")
            if function_call_result.parts[0].function_response.response == None:
                raise Exception("Empty function response response")
            # function_results.append(function_call_result.parts[0])
            print(f"-> {function_call_result.parts[0].function_response.response}")
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
