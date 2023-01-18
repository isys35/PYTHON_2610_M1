"""
Задача 3

Напишите программу, в которой описывается функция с произвольным количеством числовых аргументов, а результатом
возвращается список из трех элементов: среднее значение среди аргументов, максимальное значение среди аргументов и
минимальное значение среди аргументов.
"""
from random import randint
from statistics import mean

number_list = [randint(0, 50) for i in range(0, 10)]


def mean_max_min(*args: int) -> tuple[int]:
    """
    Функция возвращает среднее, максимальное и минимальное значения
    :param args: Произвольное количестов числовых аргументов
    :return: Среднее, максимальное и минимальное значения
    """
    return mean(*args), max(*args), min(*args)


def main():
    """Точка входа"""
    print(number_list)
    value_list = mean_max_min(number_list)
    print(value_list)


if __name__ == '__main__':
    main()