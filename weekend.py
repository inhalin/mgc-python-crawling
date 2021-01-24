import requests
from bs4 import BeautifulSoup

URL = 'http://stock.hankyung.com/apps/analysis.current?itemcode=005930'
result = requests.get(URL)
result.encoding = 'euc-kr'
soup = BeautifulSoup(result.text, "html.parser")
data_area = soup.find("div",{"class":"data_area"})
indx = data_area.find("p",{"class":"indx"})
price = indx.find("strong")

print(f"현재 시세 : {price.text}\n")

indx_list = data_area.find("dl",{"class":"indx_list"})
dts = indx_list.find_all("dt")
dds = indx_list.find_all("dd")

for i in range(len(dds)):
  print(f"{dts[i].text} : {dds[i].text}")
