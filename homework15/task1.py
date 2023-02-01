from openpyxl import Workbook
import re


def search(text):
    return re.findall(r"<author>(.*)</author>", text)


def write_xlsx(data):
    wb = Workbook()
    ws = wb.active
    for i in range(len(data)):
        ws.cell(i+1, 1, data[i])
    wb.save("Authors.xlsx")


def main():
    f = open("rss.txt", "r", encoding="utf-8")
    text = f.read()
    write_xlsx(search(text))
    f.close()


if __name__ == '__main__':
    main()
