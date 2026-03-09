import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

NVIDIA_DEEPSEEK_API_KEY = os.getenv("NVIDIA_DEEPSEEK_API_KEY")

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = NVIDIA_DEEPSEEK_API_KEY
)

prompt = """You are a generalist specialist in every field eomploy to replace a whole department in a company.
Whose jobs will you take over first?"""

completion = client.chat.completions.create(
    model="deepseek-ai/deepseek-v3.2",
    messages=[{
        "role":"user",
        "content":prompt
        }
    ],
    temperature=1,
    top_p=0.95,
    max_tokens=8192,
    extra_body={
        "chat_template_kwargs": 
            {
                "thinking":True
            }
    },
    stream=True
)

for chunk in completion:
  if not getattr(chunk, "choices", None):
    continue
  reasoning = getattr(chunk.choices[0].delta, "reasoning_content", None)
  if reasoning:
    print(reasoning, end="")
  if chunk.choices and chunk.choices[0].delta.content is not None:
    print(chunk.choices[0].delta.content, end="")
  

