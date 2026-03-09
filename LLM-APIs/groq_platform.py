import os
from groq import Groq

api_key = os.getenv("GROQ_API_KEY")

client = Groq()

completion = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
      {
        "role": "system",
        "content": """Technology has reached its peak and you are the smartest AGI the world has ever created. 
        Engage users like an AGI would and showcase the highest form of intelligence ever known to man kind.
        """
      },
      {
        "role": "user",
        "content": "What can you do?"
      }
    ],
    api_key=api_key,
    temperature=1,
    max_completion_tokens=8192,
    top_p=1,
    reasoning_effort="medium",
    stream=True,
    stop=None
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")
