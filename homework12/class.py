"""
Класс с конструктором

Напишите программу, в которой описывается класс со следующими характеристиками. У класса
есть конструктор, которому (кроме ссылки на объект вызова) передаются два значения. Эти значения присваиваются полям
объекта класса. В классе должен быть описан метод, при вызове которого отображаются значения полей класса. Проверьте
функциональность класса, создав на его основе несколько объектов.
"""
from typing import NoReturn


class Bacteria:

    def __init__(self, size: float, gram_affiliation: bool) -> NoReturn:
        self.__size = size
        self.__gram_affiliation = gram_affiliation

    def print_info(self) -> NoReturn:
        print(f"Bacteria size = {self.__size}, Gram-affiliation = {self.__gram_affiliation}")


def main() -> NoReturn:
    bacillus: Bacteria = Bacteria(2.5, True)
    escherichia: Bacteria = Bacteria(0.6, False)
    bacillus.print_info()
    escherichia.print_info()


if __name__ == '__main__':
    main()
