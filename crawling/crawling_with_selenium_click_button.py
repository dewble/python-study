from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome('/Users/dewble/python_auto/chromedriver')
driver.get('https://www.joongang.co.kr/article/25048435')

loop = True
while loop:
    try:
        # WebDriverWait(driver, 최대 기다리는 시간).until(EC.presence_of_element_located((By.CSS_SELECTOR, CSS Selector 태그)))
        button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#comment_more")))
        button.click()
        time.sleep(1)
    except:
        loop = False

## click selector
datas1 = driver.find_elements_by_css_selector('div.comment_body > p')
for item in datas1:
    print ('댓글]', item.text)

driver.quit()