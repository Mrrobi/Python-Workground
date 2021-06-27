from requests.api import head
from bs4 import BeautifulSoup
import requests
import numpy as np

res = requests.get("https://www.prothomalo.com/collection/latest")

soup = BeautifulSoup(res.text, 'lxml')

listDiv = soup.find_all('div',{"class":"customStoryCard9-m__story-data__2qgWb"})
print(len(listDiv))
heading = []
link = []
shortDet = []
for l in listDiv:
    heading.append(l.h2.text)
    link.append(l.a['href'])
    if(l.span):
        shortDet.append(l.span.text)
    else:
        shortDet.append("")

details = ["Link", "Heading", "Short Details"]

rows = []

for x in range(len(heading)):
    rows.append([])
    rows[x].append(link[x])
    rows[x].append(heading[x])
    rows[x].append(shortDet[x])

import csv 
with open('data.csv', 'a+', encoding="utf-8") as f: 
    write = csv.writer(f) 
    write.writerow(details) 
    write.writerows(rows) 