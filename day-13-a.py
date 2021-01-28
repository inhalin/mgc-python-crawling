from selenium import webdriver
from etc import driverpath as dp
import time
import csv

driver = webdriver.Chrome(dp.PATH)
PAPAGO = 'https://papago.naver.com/'
driver.get(PAPAGO)

time.sleep(3)

my_papago = open(dp.ENKO, 'r')
result = csv.reader(my_papago)

next(result)

my_dict = {}

for row in result:
  keyword = row[0]
  korean = row[1]
  my_dict[keyword] = korean

my_papago.close()

my_papago = open(dp.ENKO, 'a', newline = '')
writer = csv.writer(my_papago)

while True:
  keyword = input('번역할 영단어 입력 (0 입력시 종료) > ')
  if keyword=='0':
    print('번역종료')
    break

  if keyword in my_dict.keys():
    print(f'이미 번역한 영어단어입니다. 뜻은 {my_dict[keyword]}입니다.')
  else:
    driver.find_element_by_id('txtSource').send_keys(keyword)
    driver.find_element_by_id('btnTranslate').click()
    time.sleep(1)

    result = driver.find_element_by_id('txtTarget').text

    writer.writerow([keyword, result])
    my_dict[keyword] = result
    driver.find_element_by_id('txtSource').clear()

driver.close()
my_papago.close()

my_papago = open(dp.ENKO, 'r')
result = csv.reader(my_papago)

next(result)

for word in result:
    print(word)

my_papago.close()
