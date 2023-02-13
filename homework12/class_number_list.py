"""
Задача 8. Класс NumberList

Напишите программу, в которой описан класс. У объектов класса должно быть поле, представляющее собой числовой список.
Этот список формируется на основе списка, переданного конструктору в качестве аргумента. При этом из списка-аргумента
в список-поле включаются только числовые элементы (элементы других типов игнорируются). Необходимо также описать метод,
отображающий содержимое поля списка, а также метод, вычисляющий среднее значение элементов поля списка (сумма значений
элементов, деленная на их количество).
"""

TEST_LIST = [1, 7.0, ..., 4, 'blue', 18.60, None, 'orange', 25, 'black', 54]


class NumberList:

    def __init__(self, numbers: list):
        """
        Функция-конструктор класса создает поле обьекта состоящее только из числовых значений
        :param numbers: переданный конструктору список элементов
        """
        self.result_list: list = []
        for number in numbers:
            if isinstance(number, (float, int)):
                self.result_list.append(number)

    def show_content(self) -> list:
        """
        Функция возвращает содержимое поля обьекта
        :return: Содержимое поля списка
        """
        return self.result_list

    def mean_value(self) -> float:
        """
        Функция вычисляет среднее значение элементов поля списка
        :return: Среднее значение
        """
        mean = round(float(sum(self.result_list)/len(self.result_list)), 2)
        return mean


def main():
    """ Точка входа"""
    obj_one = NumberList(TEST_LIST)
    print(TEST_LIST)
    print(f"{obj_one.show_content()}\n"
          f"{obj_one.mean_value()}")


if __name__ == '__main__':
    main()