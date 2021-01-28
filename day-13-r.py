from selenium import webdriver
from etc import driverpath as dp
import time
import csv

driver = webdriver.Chrome(dp.PATH)
PAPAGO = 'https://papago.naver.com/'
driver.get(PAPAGO)
time.sleep(3)

my_papago = open(dp.ENKO, 'r')
table = csv.reader(my_papago)
next(table)

my_dict = {}

for row in table:
  keyword = row[0]
  korean = row[1]
  my_dict[keyword] = korean

koreans = list(my_dict.values())

result = {}

for value in koreans:
  driver.find_element_by_id('txtSource').send_keys(value)
  driver.find_element_by_id('btnTranslate').click()
  time.sleep(1)
  ko_to_en = driver.find_element_by_id('txtTarget').text
  result[value] = ko_to_en
  driver.find_element_by_id('txtSource').clear()

keys = list(result.keys())
values = list(result.values())

for key,value in zip(keys,values):
  print(f'{key} : {value}')

driver.close()
my_papago.close()

