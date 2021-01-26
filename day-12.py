import csv
from etc import driverpath as dp

count = 0

covid = open(dp.COVID_PATH, 'r')
articles = csv.reader(covid)

next(articles)

for article in articles:
  if '[속보]' in article[2]:
    print(article[2])
    count += 1

print(f"속보 기사 개수 : {count}")

covid.close()
