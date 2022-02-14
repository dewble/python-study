from selenium import webdriver

'''
selenium을 이용한 동적 웹페이지 크롤링
'''

driver_location = '/Users/dewble/python_auto/chromedriver'
driver = webdriver.Chrome(driver_location)
driver.get("https://www.joongang.co.kr/article/25048145")

titles = driver.find_elements_by_css_selector('div.comment_body > p')

for item in titles:
    print (item.text)

driver.quit()