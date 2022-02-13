import requests
from bs4 import BeautifulSoup

res = requests.get('https://dewble.com/')
soup = BeautifulSoup(res.content, 'html.parser')

datas1 = soup.select('#main > div.archive > div > div > article > h2 > a')

for item in datas1:
    print (item.get_text(), 'https://dewble.com' + item['href'])