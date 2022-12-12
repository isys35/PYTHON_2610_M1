"""
Задача 2

Напишите программу с функцией, которая аргументами получает ссылку на функцию и целое число. Результатом которой
является n-кратное исполнение переданной функции
"""
from typing import Callable


def executor(function: Callable[[int], int], n: int) -> Callable[[int], int]:
    """
    Функция, результатом которой является многократное исполнение функции.

    :param function: Вызываемая функция
    :param n: Число повторений
    :return: Callable[[int], int]
    """

    def inner(num: int) -> int:
        nonlocal n
        n -= 1
        if n < 0:
            return num
        return inner(function(num))

    return inner


def multiplier_x5(num: int) -> int:
    return num * 5


def main() -> None:
    """ Точка входа """
    print(executor(multiplier_x5, 2)(2))


if __name__ == '__main__':
    main()
