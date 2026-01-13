"""
Web scraping: Beautiful soup helps you extract data from HTML pages
"""

import requests
from bs4 import BeautifulSoup

url = "https://tesla.com"
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")

print(soup.title.text)

links = soup.find_all('a')
for link in links:
    print(link.get('href'))