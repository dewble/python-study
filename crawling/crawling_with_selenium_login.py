from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome('./chromedriver')
driver.get('http://localhost:8080/')


# login button 클릭하여 로그인 하는 경우
# WebDriverWait(driver, 최대 기다리는 시간).until(EC.presence_of_element_located((By.CSS_SELECTOR, CSS Selector 태그)))
button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#inspire > div > div > header > div > button.v-btn.v-btn--text.theme--dark.v-size--default > span")))
button.click()
button2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#list-item-32")))
button2.click()

# 다음 세 줄이 기본 패턴 코드: ID 넣기
# WebDriverWait(driver, 최대 기다리는 시간).until(EC.presence_of_element_located((By.CSS_SELECTOR, CSS Selector 태그)))
login_id = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#input-40")))
#login_id.clear() # 입력창의 경우, 사전에 작성되어 있는 텍스트를 삭제
login_id.send_keys(my_id) # 내가 넣고자 하는 텍스트 삽입

# 다음 세 줄이 기본 패턴 코드: 패스워드 넣기
login_pw = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#input-44")))
#login_pw.clear()
login_pw.send_keys(my_pw)


# 버튼 클릭시는 다음 두 줄: 로그인 버튼 누르기
button3 = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#inspire > div.v-dialog__content.v-dialog__content--active > div > div > div.v-card__actions > button.mr-5.v-btn.v-btn--is-elevated.v-btn--has-bg.theme--light.v-size--default.primary")))
button3.click()
time.sleep(2) # 로그인 후의 페이지 로딩을 위해, 1초정도 기다리면 좋음

driver.get('http://localhost:8080/post_list.html')
datas1 = driver.find_elements_by_css_selector('#inspire > div > main > div > div > div.v-data-table.elevation-1.v-data-table--has-top.v-data-table--has-bottom.theme--light > div.v-data-table__wrapper > table > tbody > tr:nth-child(1) > td:nth-child(2)')
for item in datas1:
    print (item.text)

driver.quit()