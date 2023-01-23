import asyncio
import datetime
from typing import List
import aiohttp
import xlwt
from dateutil import tz

url = "https://catalog.wb.ru/catalog/electronic15/catalog?__tmp=by&appType=1&couponsGeo=12,7,3," \
      "21&curr=byn&dest=12358386,12358403,-70563," \
      "-8139704&emp=0&lang=ru&locale=by&page={}&pricemarginCoeff=1&reg=0&regions=80,83,4,33," \
      "70,69,86,30,40,48,1,66,31,68," \
      "22&sort=popular&spp=0&subject=2872;2875"


async def parsing_site(session: aiohttp.ClientSession, page: int) -> List[str]:
    """
    Функция парсит информацию о продуктах.
    :param page: сайта
    :param session: сеанс пользователя.
    :return: Список данных о продуктах.
    """
    async with session.get(url.format(page)) as response:
        json_response = (await response.json(content_type=None))
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


async def main() -> None:
    """ Точка входа """
    async with aiohttp.ClientSession() as session:
        data = [("Name", "Price", "Date")]
        tasks = [
            parsing_site(session, page)
            for page in range(1, 11)
        ]
        done = await asyncio.gather(*tasks)
        for result in done:
            data += result

        write_to_excel(data, name="Computers", path="computers.xls")


if __name__ == '__main__':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
