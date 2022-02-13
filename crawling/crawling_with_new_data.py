import requests
from bs4 import BeautifulSoup
import pickle


def crawling_template_with_href_new(url, css_selector, pickle_name):
    return_data, all_data = list(), list()
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')

    link_titles = soup.select(css_selector)

    for num, link_title in enumerate(link_titles):
        all_data.append([link_title.get_text(), link_title['href']])  ## all_data : 지금 크롤링 한 것

    try:
        with open(pickle_name, 'rb') as file1:
            datas1 = pickle.load(file1)
    except:
        datas1 = list()  ## datas1 : 예전에 크롤링 한 것
    ## 지금 크롤링 한 것과 예전에 크롤링 한 것을 비교
    for item in all_data:
        finding = False
        for item2 in datas1:
            if item2[0] == item[0]:
                finding = True  ## 같은걸 찾으면 True로 바꾼다
                break  ## 하나라도 같은게 있으면 중단
        if finding == False:
            return_data.append(item)

    with open(pickle_name, 'wb') as file1:
        pickle.dump(all_data, file1)

    return return_data




''' 
처음 실행 시 없는 내용이라 인식하고 출력
두번째 실행 시 같은 내용이랑 빈 리스트 출력
다음 실행 시 빈 리스트와 크롤링한 내용 다름 > 출력 
'''

datas1 = crawling_template_with_href_new('https://dewble.com/', '#main > div.archive > div > div > article > h2 > a', 'drapt.txt')

with open('drapt.txt', 'wb') as file1:
    pickle.dump(datas1, file1)

for item in datas1:
    print (item)
