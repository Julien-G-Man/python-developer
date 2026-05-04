import requests
from pathlib import Path

image_url = "https://cdn-avatars.huggingface.co/v1/production/uploads/no-auth/owjKXhxqWCQvDD2KHC6lw.png"
image_path = Path("files/image.jpg")

req = requests.get(image_url)

try:
    with open(image_path, "wb") as f:
        f.write(req.content)
    print(f"Image downloaded at {image_path}")
except Exception as e:
    print(e)