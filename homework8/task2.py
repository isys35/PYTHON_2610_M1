"""
Задача 2
Напишите программу с функцией, аргументом, которой передается
числовой список, а результатом является еще один список, в который
включены только нечетные числа из списка-аргумента.
"""

from random import randint


def list_generation(amount_elements: int) -> list[int]:
    """
    Функция генерирующая входящий список
    :param amount_elements: количество элементов списка
    :return: list[int]
    """
    list1 = []
    for i in range(amount_elements):
        list1.append(randint(1, 100))
    return list1


def odd_list(unsorted: list[int]) -> list[int]:
    """
    Функция, сортирующая входящий список и возвращающая список нечетных элементов
    :param unsorted:
    :return:
    """
    return [i for i in unsorted if i % 2 != 0]


if __name__ == '__main__':
    list1 = list_generation(10)
    sort_list = odd_list(list1)
    print(list1)
    print(sort_list)
