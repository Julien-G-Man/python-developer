import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "Explain the history of the PayPal Mafia,"}
    ]
)

resp = response["choices"][0]["messages"]["content"]
print(resp)