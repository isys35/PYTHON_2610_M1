"""
Задача 1

Напишите программу, в которой используется функция-генератор, создающая итерируемый объект с названиями месяцев.
"""
from typing import Tuple, Generator

ALL_MONTHS = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December")


def months_generator(months: Tuple[str, ...]) -> Generator[str, None, None]:
    """
    Функция возвращает генератор месяцев.
    :param months: Месяцы
    :return: Generator
    """
    for month in months:
        yield month


def main() -> None:
    """ Точка входа """

    for month in months_generator(ALL_MONTHS):
        print(month)


if __name__ == '__main__':
    main()
