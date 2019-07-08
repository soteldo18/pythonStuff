import requests
from bs4 import BeautifulSoup
r = requests.get('https://github.com')
title_text=''
if r.status_code == 200:
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find_all('p')
    if title is not None:
       title_text = title[1].text.strip()
print(title_text)

