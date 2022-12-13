"""
Задача 3
Напишите программу, в которой описывается функция с произвольным количеством числовых аргументов, а результатом
возвращается список из трех элементов: среднее значение среди аргументов, максимальное значение среди аргументов и
минимальное значение среди аргументов.
"""

from statistics import mean


def mean_min_max(*args: tuple) -> tuple[float, float, float]:
    """
    Функция находит минимум, максимум и среднее значение списка
    :param args: кортеж чисел
    :return: tuple[float, float, float]
    """
    return min(*args), max(*args), mean(*args)


def main() -> None:
    """Точка входа"""
    number = (2, 9, 0, 5, -5, 1, 7, -8)
    print(mean_min_max(number))


if __name__ == '__main__':
    main()
