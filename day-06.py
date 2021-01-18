import requests
from bs4 import BeautifulSoup

URL = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=1"
result = requests.get(URL)
soup = BeautifulSoup(result.text, "html.parser")
tbody = soup.find("tbody")
print(tbody)