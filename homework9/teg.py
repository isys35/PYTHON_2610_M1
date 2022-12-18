"""
Задача 3.

Напишите функцию-декоратор, чтобы она  заключала возвращаемое значение упакованной функции в теги "<html>" и "</html>"
Обернутая функция должна возвращать подобный результат:

<html>hello<html>
"""


def html(func):
    """
    Функция-декоратор
    :param func: функция для обертывания
    :return: обернутая функция
    """
    def wrapper(*args):
        def inner(*args):
            val = func(*args)
            return "<html>{}</html>".format(val)
        return inner(*args)
    return wrapper


@html
def get_tag(text):
    """
    Функция приветсвия.
    :param text: переменная с текстом приветсвия
    :return: text
    """
    return text


if __name__ == '__main__':
    print(get_tag("Hello"))
