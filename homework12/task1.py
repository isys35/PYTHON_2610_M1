"""Напишите программу, в которой описывается класс со следующими характеристиками.
У класса есть конструктор, которому (кроме ссылки на объект вызова) передаются два
значения. Эти значения присваиваются полям объекта класса. В классе должен быть
описан метод, при вызове которого отображаются значения полей класса. Проверьте
функциональность класса, создав на его основе несколько объектов."""


class Books:
    def __init__(self, book_tite, author):
        self.book_title = book_tite
        self.author = author

    def printf(self):
        print(f"Book title - {self.book_title} / author - {self.author}")


def main():
    b1 = Books("The Martian", "Andy Weir")
    b2 = Books("Spin", "Wilson")
    b1.printf()
    b2.printf()


if __name__ == '__main__':
    main()
