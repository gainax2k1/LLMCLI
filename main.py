import os
import sys #to recieve CLI prompts

from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

if len(sys.argv) < 2:
    exit(1)

verbose = False

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
    contents=messages
)

if verbose:
    print(f"Working on: {user_prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

print(response.text)
