"""
Напишите программу, в которой описан класс. У объектов класса должно быть поле, представляющее собой числовой список.
Этот список формируется на основе списка, переданного конструктору в качестве аргумента. При этом из списка-аргумента
в список-поле включаются только числовые элементы (элементы других типов игнорируются). Необходимо также описать метод,
отображающий содержимое поля списка, а также метод, вычисляющий среднее значение элементов поля списка (сумма значений
элементов, деленная на их количество).
"""

from statistics import mean
from typing import Any, List


class NumberList:

    def __init__(self, data_list: List[Any]) -> None:
        self.number_list = [x for x in data_list if isinstance(x, int)]

    def get_number_list(self) -> List:
        return self.number_list

    def mean_number_list(self) -> float:
        return mean(self.number_list)


def main():
    data_list: NumberList = NumberList(['Hello', 1, 3, 15, 7, 2])
    print(data_list.get_number_list())
    print(data_list.mean_number_list())


if __name__ == '__main__':
    main()
