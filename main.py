import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info


def main():

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    # count = 0
    # for arg in sys.argv:
    #     print(f"Argument {count}: {arg}")
    #     count += 1

    try:
        prompt = sys.argv[1]
    except Exception:
        print('Error: No prompt provided.')
        print('\nAI Assistant (using Gemini)')
        print('usage: python main.py "AI prompt here"')
        print('example: "WTF does \'skibidi\' mean?"\n') 
        return sys.exit(1)

    model_name='gemini-2.0-flash-001'

    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]

    system_prompt = """
        You are a helpful AI coding agent.

        When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

        - List files and directories

        All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
        """

    # print(f" --> schema_get_files_info: {schema_get_files_info}")

    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
        ]
    )

    ai_config = types.GenerateContentConfig(tools=[available_functions], 
                                            system_instruction=system_prompt)

    response = client.models.generate_content(model=model_name,
                                              contents=messages,
                                              config=ai_config)

    
    report = ''

    print("---- ai-agent ----")
    function_calls = response.function_calls
    if len(function_calls):
        for part in function_calls:
            report += f"Calling function: {part.name}({part.args})"
    else:
        text_out = response.text
        report += f"\nResponse from gemini:\n {text_out}"

    pcount = response.usage_metadata.prompt_token_count
    tcount = response.usage_metadata.candidates_token_count

    if "--verbose" in sys.argv:
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {pcount}")
        print(F"Response tokens: {tcount}")
    
    print(report)

    return report

if __name__ == "__main__":
    main()
