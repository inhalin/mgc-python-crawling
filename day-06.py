import requests
from bs4 import BeautifulSoup

URL = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=1"
result = requests.get(URL)
soup = BeautifulSoup(result.text, "html.parser")  # 문자열 html코드로 가져오기
tbody = soup.find("tbody")

a = tbody.find_all("a",{"class":"tltle"})  # 종목명 가져오기
stocks = []
for i in range(len(a)):
  stocks.append(a[i].text)  # 태그 안의 내용만 stocks 리스트에 담기

td = tbody.find_all("td",{"class":"number"}) # 항목 가져오기
numbers = []
for i in range(len(td)):
  numbers.append(td[i].text.strip())  # 태그 안의 내용만 numbers 리스트에 담기

# 분할갯수=10, 한 종목당 10개 항목이기 때문에 10개씩 분할해 넣어준다.
n=10

# 10개 항목씩 분할해 넣기
numbers = [numbers[i * n:(i + 1) * n] for i in range((len(td)+n-1)//n)]

kosdaq = {}
for i in range(50):
  kosdaq[stocks[i]]=numbers[i]  # key:종목, value: 항목 10개

print(kosdaq)

