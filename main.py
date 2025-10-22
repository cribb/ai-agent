import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


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

    model='gemini-2.0-flash-001'
    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]

    response = client.models.generate_content(model=model,
                                              contents=messages)

    print("Hello from ai-agent!")
    print(f"\nResponse from gemini:\n {response.text}")

    X = response.usage_metadata.prompt_token_count
    Y = response.usage_metadata.candidates_token_count

    print(f"Prompt tokens: {X}")
    print(F"Response tokens: {Y}")


if __name__ == "__main__":
    main()
