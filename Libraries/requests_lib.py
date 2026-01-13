"""
'requests' makes it easy to send HTTO requests
"""

import requests

response = requests.get("https://api.github.com")
status = response.status_code

print(f'Response: {response}')
print(f'Status: {status}')
print(f'JSON: {response.json}')

# fetch and print IP address
res = requests.get("https://api.ipify.org?format=json")
print(res.json()['ip'])