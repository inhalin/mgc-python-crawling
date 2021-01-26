from selenium import webdriver
from etc import driverpath as dp
import time

result = {}

driver = webdriver.Chrome(executable_path = dp.PATH)
PAPAGO = 'https://papago.naver.com/'
driver.get(PAPAGO)
time.sleep(2)

def get_papago_result():
  for i in range(5):
    query = input("번역할 영어단어 > ")
    time.sleep(1)
    driver.find_element_by_id('txtSource').send_keys(query)
    driver.find_element_by_id('btnTranslate').click()
    time.sleep(1)
    value = driver.find_element_by_id('txtTarget').text
    result[query] = value
    driver.find_element_by_id('txtSource').clear()

get_papago_result()

print(result)
driver.close()