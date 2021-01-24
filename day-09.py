import requests
from bs4 import BeautifulSoup
import time

# t1=time.monotonic()
# keyword='코로나'

print("<< 한국경제 최근 기사 검색 >>")
terminate="exit"

while True:
  print(f"프로그램을 종료하려면 {terminate}을 입력하세요.")
  print("-"*40)

  keyword = input("뉴스 검색어를 입력하세요 > ")

  if keyword==terminate:
    break

  count=0
  URL = f"https://search.hankyung.com/apps.frm/search.news?query={keyword}&mediaid_clust=HKPAPER,HKCOM"
  no_result = True

  for page in range(1,3):
    result = requests.get(f"{URL}&page={page}")
    soup = BeautifulSoup(result.text, "html.parser")

    # 뉴스 기사 제목
    titles = soup.find_all("em",{"class":"tit"})

    # 기사 작성 날짜 및 시간
    dates = soup.find_all("span",{"class":"date_time"})

    # 검색결과 없을때 태그
    search_none = soup.find("div",{"class":"search_none"})

    # 검색결과 있으면 no_result 를 False 로 설정
    if search_none==None:
      no_result = False

    for i in range(len(titles)):
      count += 1
      print(f"{count} - [ {dates[i].text.strip()} ] {titles[i].text.strip()}")

  if no_result:
    print(search_none.text.strip())

  print()

# t2 = time.monotonic()
# print(f"diff:{t2-t1}")
# 검색어 코로나로 프로그램 실행시 평균 0.9초