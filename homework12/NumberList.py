"""
Класс NumberList

Напишите программу, в которой описан класс. У объектов класса должно быть поле, представляющее
собой числовой список. Этот список формируется на основе списка, переданного конструктору в качестве аргумента. При
этом из списка-аргумента в список-поле включаются только числовые элементы (элементы других типов игнорируются).
Необходимо также описать метод, отображающий содержимое поля списка, а также метод, вычисляющий среднее значение
элементов поля списка (сумма значений элементов, деленная на их количество).
"""
from statistics import mean
from typing import Any, NoReturn, List


class NumberList:

    def __init__(self, data_list: List[Any]) -> NoReturn:
        self.number_list = []
        self.number_list = list(filter(lambda x: type(x) == float or type(x) == int, data_list))

    def get_numbers_list(self) -> List:
        return self.number_list

    def mean_numbers_list(self) -> float:
        return mean(self.number_list)


def main():
    data_list: NumberList = NumberList([1, 2, 3.5, 4, "Привет"])
    print(data_list.get_numbers_list())
    print(data_list.mean_numbers_list())


if __name__ == '__main__':
    main()
