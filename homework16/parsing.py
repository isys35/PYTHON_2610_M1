from typing import List
from dateutil import tz
import requests
import datetime
import xlwt


def parsing_wb(url: str):
    response = requests.get(url)
    json_response = response.json()
    date_header: datetime.date = datetime.datetime.strptime(response.headers['Date'], '%a, %d %b %Y %H:%M:%S %Z')
    date: str = convert_time(date_header)
    data: List = []
    for product in json_response["data"]["products"]:
        data.append((product["name"], product["salePriceU"] / 100, date))
    return data


def convert_time(date) -> str:
    date_utc = date.replace(tzinfo=tz.gettz("UTC"))
    date_timezone = date_utc.astimezone(tz.gettz('Europe/Minsk'))
    date_now: str = date_timezone.strftime('%d%m%y %H:%M:%S')
    return date_now


def write_to_excel(data, name: str, path: str):
    book = xlwt.Workbook(encoding="utf-8")
    sheet = book.add_sheet(name)
    for row in range(len(data)):
        for column in range(len(data[row])):
            sheet.write(row, column, data[row][column])
    book.save(path)


def main():
    data = [("Name", "Price", "Date")]
    for page in range(1, 11):
        url = f"https://catalog.wb.ru/catalog/electronic15/catalog?subject=2872;2875&limit=100&sort=popular&page=" \
              + str(page) + "&appType=128&curr=byn&locale=by&lang=ru&dest=12358386,12358404,3,-59208&regions=1,4,22," \
                            "30,31,33,40,48,66,68,69,70,80," \
                            "83&emp=0&reg=1&pricemarginCoeff=1.0&offlineBonus=0&onlineBonus=0&spp=0 "
        data += parsing_wb(url)

    write_to_excel(data, name="Computers", path="computers.xls")


if __name__ == '__main__':
    main()
