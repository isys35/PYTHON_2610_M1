"""
Задача 3. Декоратор для создания тегов

Напишите функцию-декоратор, чтобы она заключала возвращаемое значение упакованной функции в теги "<html>" и "</html>"
Обернутая функция должна возвращать подобный результат: <html>hello<html>
"""


def decorator_for_tags(func) -> str:
    """
    Функция-декоратор упаковывает значение в теги
    :param func: Функция передаваемая в декоратор качестве аргумента
    :return: Упакованное в теги значение
    """
    def wrapper(arg):
        in_tags = f"<html>{func(arg)}<html>"
        return in_tags

    return wrapper


@decorator_for_tags
def hello(message: str) -> str:
    """
    Функция получается и возвращает некоторое текстовое сообщение
    :param message: Передаваемое в качестве аргумента сообщение
    :return: Полученное сообщение
    """
    return message


def main():
    """ Точка входа"""
    print(hello("First page"))


if __name__ == '__main__':
    main()
