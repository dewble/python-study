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



res = requests.get('https://dewble.com')
print("### res.headers")
print(res.headers['content-type'])

print()
print("### crawling_bak method")
result = crawling('https://dewble.com','div > article > h2')
#print(result)

for item in result:
    print(item)

    # main > div.archive > div > div:nth-child(1) > article > h2