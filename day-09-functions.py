import requests
from bs4 import BeautifulSoup
import time

# t1=time.monotonic()
# keyword='코로나'

keyword = input("뉴스 검색어를 입력하세요 > ")
count=0
URL = f"https://search.hankyung.com/apps.frm/search.news?query={keyword}&mediaid_clust=HKPAPER,HKCOM"

def getTitles():
  titles = []
  for page in range(1,3):
    result = requests.get(f"{URL}&page={page}")
    soup = BeautifulSoup(result.text, "html.parser")

    # 뉴스 기사 제목
    news_titles = soup.find_all("em",{"class":"tit"})

    for i in range(len(news_titles)):
      titles.append(news_titles[i].text.strip())

  return titles

def getDates():
  dates = []
  for page in range(1,3):
    result = requests.get(f"{URL}&page={page}")
    soup = BeautifulSoup(result.text, "html.parser")

    # 기사 작성 날짜 및 시간
    news_dates = soup.find_all("span",{"class":"date_time"})

    for i in range(len(news_dates)):
      dates.append(news_dates[i].text.strip())

  return dates

final_titles=getTitles()
final_dates=getDates()

if len(getTitles())==0:
  print(f"'{keyword}'에 대한 검색결과가 없습니다.")
else:
  for i in range(len(getTitles())):
    count += 1
    print(f"{count} - [ {final_dates[i]} ] {final_titles[i]}")

# t2 = time.monotonic()
# print(f"diff:{t2-t1}")
# 검색어 코로나로 프로그램 실행시 평균 3.5초
