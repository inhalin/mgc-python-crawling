from selenium import webdriver
from etc import driverpath as dp
import time
import csv

driver = webdriver.Chrome(dp.PATH)
PAPAGO = 'https://papago.naver.com/'
driver.get(PAPAGO)

time.sleep(3)

my_papago = open(dp.ENKO, 'w', newline='')
writer = csv.writer(my_papago)
writer.writerow(['영단어','번역결과'])

while True:
  keyword = input('번역할 영단어 입력 (0 입력시 종료) > ')
  if keyword=='0':
    print('번역종료')
    break

  driver.find_element_by_id('txtSource').send_keys(keyword)
  driver.find_element_by_id('btnTranslate').click()
  time.sleep(1)

  result = driver.find_element_by_id('txtTarget').text

  writer.writerow([keyword, result])
  driver.find_element_by_id('txtSource').clear()

driver.close()
my_papago.close()