import requests
api = "http://localhost:8000"
body = {"text": "A great  movie"}
response = requests.post(api, json=body)