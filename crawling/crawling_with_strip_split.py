import requests
from bs4 import BeautifulSoup


def crawling(url, css_selector):
    return_data = list()
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    datas1 = soup.select(css_selector)
    for item in datas1:
        return_data.append(item.get_text())
    return return_data


result = crawling('https://dewble.com','#main > div.archive > div > div > article > h2 > a')

for item in result:
  print(item.split(')')[-1].strip())