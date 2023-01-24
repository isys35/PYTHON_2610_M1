"""Напишите программу, в которой описан класс. У объектов класса должно быть поле,
представляющее собой числовой список. Этот список формируется на основе списка,
переданного конструктору в качестве аргумента. При этом из списка-аргумента в список-поле
включаются только числовые элементы (элементы других типов игнорируются). Необходимо
также описать метод, отображающий содержимое поля списка, а также метод, вычисляющий
среднее значение элементов поля списка (сумма значений элементов, деленная на их количество)."""

from statistics import mean
from typing import Any, List


class NumberList:
    def __init__(self, data: List[Any]):
        self.list = [i for i in data if isinstance(i, (float, int))]

    def printf(self):
        print(self.list)

    def mean_of_the_list(self):
        print(mean(self.list))


def main():
    data: NumberList = NumberList([1, 5, "d", 2.3, 'qq', 0])
    data.printf()
    data.mean_of_the_list()


if __name__ == '__main__':
    main()
