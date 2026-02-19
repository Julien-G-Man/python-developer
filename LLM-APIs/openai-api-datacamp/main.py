import os
import logging
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI()

def call_openai(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            max_completions_token=100,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        result = response.choices[0].message.content
    
        return result
    except Exception as e:
        return e

# prompt = input("Enter a prompt: ") # prompt = "How do you call a developer who uses the OpenAI API profeciently?"

history = []

def persist_history(prompt, ai_response):
    history.append({"prompt": prompt, "ai_response": ai_response})
    
    return history


if __name__ == "__main__":
    prompt, ai_response = None, None
    
    for i in range(5, -1, -1):
        history = persist_history(prompt, ai_response)
        
        if i == 0:
            print("You've exhausted all you trials\n")
            print(f"History: {history}")
            break
        
        prompt = input("Enter a prompt: ")
        if i < 5:
            new_prompt = f"User asked: '{prompt}'. \nHere's the discussion so far: \n {history.reverse()}"
            call_openai(new_prompt)
        else:          
            ai_response = call_openai(prompt)
            call_openai(prompt)
        
        ai_response = call_openai(prompt)
        persist_history(prompt, ai_response)
        
        print(f"\nYou have {i-1} more trial(s). \n")
        