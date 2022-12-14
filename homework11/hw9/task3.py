"""
Напишите функцию-декоратор, чтобы она заключала возвращаемое
значение упакованной функции в теги "<html>" и "</html>"

"""
from typing import Callable


def html(func: Callable[[str], str]) -> Callable[[str], None]:
    def wrapper(*args):
        def inner(*args):
            val = func(*args)
            return "<html>{}</html>".format(val)
        return inner(*args)
    return wrapper


@html
def plus_html(text) -> str:
    """
    Функция возвращает введенный текст
    :param text: строка
    :return: str
    """
    return text


def main() -> None:
    print(plus_html("Hello"))


if __name__ == '__main__':
    main()
