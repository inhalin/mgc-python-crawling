from selenium import webdriver
from etc import driverpath as dp
import time

LOGIN_URL = 'https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com'

driver = webdriver.Chrome(dp.PATH)
driver.get(LOGIN_URL)
time.sleep(2)

driver.execute_script("document.getElementsByName('id')[0].value = \'" + dp.ID + "\'")
driver.execute_script("document.getElementsByName('pw')[0].value = \'" + dp.PW + "\'")
time.sleep(1)

driver.find_element_by_id('log.login').click()
time.sleep(1)

COMU_URL = 'https://cafe.naver.com/codeuniv'
driver.get(COMU_URL)
time.sleep(1)

driver.find_element_by_id('menuLink90').click()
time.sleep(1)

driver.switch_to.frame('cafe_main')
time.sleep(1)

driver.find_element_by_xpath('//*[@id="main-area"]/div[4]/table/tbody/tr[1]/td[1]/div[2]/div/a').click()
time.sleep(1)

for i in range(20):
  title = driver.find_element_by_class_name('title_text').text
  nickname = driver.find_element_by_class_name('nickname').text
  date = driver.find_element_by_class_name('date').text
  content = driver.find_element_by_css_selector('div.se-component-content').text
  print(f'[{i+1}번 게시글]\n제목 : {title}\n닉네임 : {nickname}\n작성일 : {date}\n내용 : {content}\n')

  driver.find_element_by_class_name("btn_next").click()
  time.sleep(1)

driver.close()