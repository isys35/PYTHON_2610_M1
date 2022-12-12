"""
Задача 3

Напишите функцию-декоратор, чтобы она заключала возвращаемое значение упакованной функции в теги "<html>" и "</html>"
"""

from homework9.decorators import html_template


@html_template
def greetings(name: str) -> str:
    """
    Функция возвращает приветствие для пользователя
    :param name: Имя пользователя
    :return: str
    """
    return f"Hello {name}"


def main() -> None:
    """ Точка входа """
    greetings("Max")


if __name__ == '__main__':
    main()
