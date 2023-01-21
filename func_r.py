import requests
from bs4 import BeautifulSoup
import re
import  openpyxl as ox


URL = "https://docs.google.com/document/d/1Y6Dj4oAGjq2Y0VxufQ69udLD_f0f1KxbT5mTzFDQRXA/edit?usp=sharing"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text,  'lxml')
soup = str(soup)


authors = re.findall(r'\\u003cauthor\\u003e([\s\S]*?)\\u003c/author\\u003e', soup)

for item in authors:
    print(item)

wb = ox.Workbook()
ws = wb.worksheets[0]

for i, statN in enumerate(authors):
    ws.cell(column=1, row=i + 1).value = statN
    wb.save('some.xlsx')

