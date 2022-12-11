"""
Задача 3

Напишите программу, в которой описывается функция с произвольным количеством числовых аргументов, а результатом
возвращается список из трех элементов: среднее значение среди аргументов, максимальное значение среди аргументов и
минимальное значение среди аргументов.
"""

from statistics import mean


def statistical_analysis(*args: tuple) -> tuple[float, float, float]:
    """
    Функция находит минимум, максимум и среднее значение списка.
    :param args: Кортеж чисел
    :return: tuple[float, float, float]
    """
    return mean(*args), min(*args), max(*args)


def main() -> None:
    """ Точка входа """
    numbers = (1, 2, -6, 10)
    print(statistical_analysis(numbers))


if __name__ == '__main__':
    main()
