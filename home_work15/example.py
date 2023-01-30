'''Написать скрипт, который из файла rss.txt достает информацию из тега <author></author>
c помощью регулярных выражений, и  полученную информацию сохраняет в excel файл'''

from openpyxl import Workbook
import re


def search(text):
    return re.findall(r'<author>(.*)</author>', text)


def write_xlsx(data):
    wb = Workbook()
    ws = wb.active
    for i in range(len(data)):
        ws.cell(i + 1, 1, data[i])
    wb.save("test.xlsx")


def main():
    with open('rss.txt', 'r', encoding='utf-8') as file:
        text: str = file.read()
        write_xlsx(search(text))


if __name__ == '__main__':
    main()
