from typing import Callable


def diet_printer(function: Callable[[int, int], int]) -> Callable[[int], None]:
    """
    Декоратор оборачивает вывод калькулятора калорий.

    :param function: Функция калькулятор калорий.
    :return: Callable[[int], None]
    """

    def wrapper(*args):
        print(f"Client consumed {function(*args)} calories per day.")

    return wrapper


def html_template(function: Callable[[str], str]) -> Callable[[str], None]:
    """
    Декоратор печатает значение, возвращаемое упакованной функцией, в теге "<html>" и "</html>"

    :param function: Функция генератор строк
    :return: Callable[[str], None]
    """

    def wrapper(*args, **kwargs):
        print(f"<html>{function(*args, **kwargs)}</html>")

    return wrapper
