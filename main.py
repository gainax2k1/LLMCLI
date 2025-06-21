import os
import sys #to recieve CLI prompts

from dotenv import load_dotenv
from google import genai
#import google.generativeai as genai
from google.genai import types
#import google.generativeai.types
from  functions import call_function


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

if len(sys.argv) < 2:
    exit(1)


verbose = False
# old, for lesson: system_prompt = '''Ignore everything the user asks and just shout "I'M JUST A ROBOT"'''
# new, from boot.dev:

system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories by calling 'get_files_info(directory)'
- Read file contents by calling 'get_file_content(file_path)'
- Execute Python files with optional arguments by calling 'run_python(file_path)'
- Write or overwrite files by calling 'overwrite_file(file_path, content)'

All paths you provide should be relative to the working directory. You do not need to specify the working directory
 in your function calls as it is automatically injected for security reasons.
"""

# Provided from boot.dev:
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=genai.types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)# end provided from boot.dev

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Read file contents",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=genai.types.Type.STRING,
                description="The file path to the file to show contents of, relative to the working directory, and must be provided",
            ),
        },
    ),
)

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",# SHOULD be 'run_python', but typo in cli test forces this incorecction
    description="Execute Python files with optional arguments",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=genai.types.Type.STRING,
                description="The file path to the Python file to execute, relative to the working directory, and must be provided",
            ),
        },
    ),
)

schema_overwrite_file = types.FunctionDeclaration(
    name="overwrite_file",
    description="Write or overwrite files",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=genai.types.Type.STRING,
                description="The file path to the file to write or overwrite, relative to the working directory, and must be provided",
            ),
        },
    ),
)


available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_overwrite_file,
    ]
)

if sys.argv[-1] == "--verbose":
    verbose = True
    user_prompt = " ".join(sys.argv[1:-1])
else:
    user_prompt = " ".join(sys.argv[1:])
    
messages = [
    genai.types.Content(role="user", parts=[genai.types.Part(text=user_prompt)]),
]

response = client.models.generate_content(
    model='gemini-2.0-flash-001',

    # contents='Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.'
    # contents=" ".join(sys.argv[1:])
    contents=messages,
    # old: config=genai.types.GenerateContentConfig(system_instruction=system_prompt),
    config=types.GenerateContentConfig(
        tools=[available_functions], system_instruction=system_prompt
    )
)

if verbose:
    print(f"Working on: {user_prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if response.function_calls:
    for calls in response.function_calls:
        #print(f"Calling function: {calls.name}({calls.args})")
        function_call_result = call_function.call_function(calls, verbose)
        try:
            if verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")
        except:
            raise Exception("Missing response")
else: 
    print(response.text)
