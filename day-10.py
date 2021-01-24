from selenium import webdriver
import time
from etc import driverpath as dp

driver = webdriver.Chrome(dp.PATH)
NAVER_URL = 'https://www.naver.com'

query='리팩토링'

driver.get(NAVER_URL)
driver.find_element_by_id('query').send_keys(query)
driver.find_element_by_id('search_btn').click()

queryurl = driver.current_url

time.sleep(2)
driver.close()

print(queryurl)