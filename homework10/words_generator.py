"""
Задача 2
Написать функцию-генератор для выделения слов из текста (слова разделяются пробелом, либо переносом строки ‘\n’).
Список всех слов при этом в функции не создавать. """

import re
from typing import Generator


def words_generator(string: str) -> Generator[str, str, None]:
    """
    Функция выделяет слова из текста.

    :param string: Текст
    :return: Generator[str, str, None]
    """

    word = ""
    for letter in string:
        if re.match(r'\w', letter):
            word += letter
        elif len(word) > 0:
            yield word
            word = ""
    yield word


def main() -> None:
    """ Точка входа """

    for item in words_generator("Lorem ipsum, dolor sit\namet!!!"):
        print(item)


if __name__ == '__main__':
    main()
