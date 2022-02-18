import requests
from bs4 import BeautifulSoup

'''
res = requests.get('https://dewble.com/')
soup = BeautifulSoup(res.content, 'html.parser')

datas1 = soup.select('#main > div.archive > div > div > article > h2 > a')

for item in datas1:
    print (item.get_text(), 'https://dewble.com' + item['href'])
'''


def crawling_with_link(url, css_selector, pre_url):
    return_data = list()
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    datas1 = soup.select(css_selector)
    for item in datas1:
        return_data.append([item.get_text(), pre_url + item['href']])
    return return_data

datas1 = crawling_with_link('http://www.drapt.com/e_sale/index.htm?page_name=esale_news&menu_key=34', 'a.c0000000', 'http://www.drapt.com/e_sale/')

for item in datas1:
  print(item)