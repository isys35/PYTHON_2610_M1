"""
Написать скрипт, который из файла rss.txt достает информацию из тега <author></author> c помощью регулярных выражений,
и  полученную информацию сохраняет в excel файл
"""
import re
from typing import List

import xlwt


def reading_file(way: str):
    with open(way, "r", encoding='utf-8') as f:
        text: str = f.read()
        return text


def write_excel(data: List[List[str]], name: str, way: str):
    book = xlwt.Workbook(encoding="utf-8")
    sheet = book.add_sheet(name)
    for row in range(len(data)):
        for column in range(len(data[row])):
            sheet.write(row, column, data[row][column])

    book.save(way)


def search_authors(authors: List[str]):
    sheet: List = []
    for row in range(len(authors)):
        if authors[row].lower().find("отдел") >= 0:
            sheet.append([authors[row]])
        else:
            sheet.append(re.split(r'\s+', authors[row]))
    return sheet


def main():
    text = reading_file("./rss.txt")
    authors: List[str] = re.findall(r'<author>(.*)</author>', text)
    write_excel(search_authors(authors), "Author", "author.xls")


if __name__ == '__main__':
    main()