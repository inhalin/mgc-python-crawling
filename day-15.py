from selenium import webdriver
from etc import driverpath as dp
import time

keyword = input('검색할 뉴스 키워드를 입력하세요 > ')
driver = webdriver.Chrome(dp.PATH)
pages = ['1','2','3']
count = 0

for page in pages:
  URL = f'https://search.hankyung.com/apps.frm/search.news?query={keyword}&mediaid_clust=HKPAPER,HKCOM&page={page}'
  driver.get(URL)
  time.sleep(2)

  ten_articles = driver.find_elements_by_css_selector('em.tit')

  for article in ten_articles:
    title = article.text

    article.click()
    time.sleep(1)

    driver.switch_to.window(driver.window_handles[-1])

    content = driver.find_element_by_id('articletxt').text
    seperate = content.split('\n')

    count += 1
    print(f'< {count}번 뉴스 - {title} >')
    for sep in seperate:
      if sep != '':
        print(sep, end = ' ')
    print('\n')

    driver.close()

    driver.switch_to_window(driver.window_handles[0])
    time.sleep(1)

driver.close()

