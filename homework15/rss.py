"""
Собрать данные из файла и сохранить в excel

Написать скрипт, который из файла rss.txt достает информацию из тега <author></author> c помощью регулярных
выражений, и полученную информацию сохраняет в excel файл
"""
import re
from typing import List

import xlwt


def read_file(path: str) -> str:
    """
    Функция читает данные из файла.

    :param path: путь к файлу.
    :return: содержимое файла
    """
    with open(path, "r", encoding='utf-8') as f:
        text: str = f.read()
        return text


def write_to_excel(data: List[List[str]], name: str, path: str) -> None:
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


def handle_authors(authors: List[str]) -> List[List[str]]:
    """
    Функция ищет авторов.
    :param authors: авторы
    :return: Таблицу данных
    """
    sheet: List = []
    for row in range(len(authors)):
        if authors[row].lower().find("отдел") >= 0:
            sheet.append([authors[row]])
        else:
            sheet.append(re.split(r'\s+', authors[row]))
    return sheet


def main() -> None:
    """ Точка входа """
    try:
        text = read_file("./rss.txt")
        authors: List[str] = re.findall(r'<author>(.*)</author>', text)
        write_to_excel(handle_authors(authors), "Author", "author.xls")
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("Unexpected error: ", e)


if __name__ == '__main__':
    main()
