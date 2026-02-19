import requests
import json

url = "http://127.0.0.1:5000"

response = requests.post(f"{url}/drinks/1")
print(response.json())