import datetime
from typing import List

import requests
import xlwt
from dateutil import tz


def parsing_site(url: str) -> List[str]:
    """
    Функция парсит информацию о продуктах.
    :param url: адрес сайта
    :return: Список данных о продуктах.
    """
    response = requests.get(url)
    json_response = response.json()
    date_header: datetime.date = datetime.datetime.strptime(response.headers['Date'], '%a, %d %b %Y %H:%M:%S %Z')
    date: str = convert_time(date_header)
    data: List = []
    for product in json_response["data"]["products"]:
        data.append((product["name"], product["salePriceU"] / 100, date))
    return data


def convert_time(date) -> str:
    """
    Функция конвертирует часовые пояса.
    :param date: Время запроса.
    :return: Время в нужном формате.
    """
    date_utc = date.replace(tzinfo=tz.gettz("UTC"))
    date_timezone = date_utc.astimezone(tz.gettz('Europe/Minsk'))
    date_new: str = date_timezone.strftime('%d/%m/%y %H:%M:%S')
    return date_new


def write_to_excel(data, name: str, path: str) -> None:
    """
    Функция записывает данные в Excel-таблицу.
    :param data: таблица данных
    :param name: название листа
    :param path: путь к файлу результата
    :return: none
    """
    book = xlwt.Workbook(encoding="utf-8")
    sheet = book.add_sheet(name)
    for row in range(len(data)):
        for column in range(len(data[row])):
            sheet.write(row, column, data[row][column])

    book.save(path)


def main() -> None:
    """ Точка входа """
    data = [("Name", "Price", "Date")]
    for page in range(1, 11):
        url = f"https://catalog.wb.ru/catalog/electronic15/catalog?__tmp=by&appType=1&couponsGeo=12,7,3," \
              "21&curr=byn&dest=12358386,12358403,-70563," \
              "-8139704&emp=0&lang=ru&locale=by&page=" + str(page) + "&pricemarginCoeff=1&reg=0&regions=80,83,4,33," \
                                                                     "70,69,86,30,40,48,1,66,31,68," \
                                                                     "22&sort=popular&spp=0&subject=2872;2875 "
        data += parsing_site(url)

    write_to_excel(data, name="Computers", path="computers.xls")


if __name__ == '__main__':
    main()
