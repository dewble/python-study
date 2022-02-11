import requests
from bs4 import BeautifulSoup

res = requests.get('http://www.drapt.com/e_sale/index.htm?page_name=esale_news&menu_key=34')
soup = BeautifulSoup(res.content, 'html.parser')

datas1 = soup.select('a.c0000000')

for item in datas1:
    print (item.get_text(), 'http://www.drapt.com/e_sale/' + item['href'])