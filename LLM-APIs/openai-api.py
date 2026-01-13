import openai
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

def call_openai(user_input):
    try:
        response = client.responses.create(
            model="gpt-4o-mini",
            input = user_input
        )
        result = response.output_text
        print(result)
        return result
    except Exception as e:
        print(f"Error calling OpenAI API: {e}")

user_input="Hello, how are you doing?" # input("User input: ")

if __name__ == "__main__":
    call_openai(user_input)