"""
Написать функцию-генератор для выделения слов из текста (слова разделяются пробелом,
либо переносом строки ‘\n’). Список всех слов при этом в функции не создавать.

"""


def generate_words(a: str) -> str:
    """
    Функция выделяет слова из текста
    :param a: текст
    :return: str
    """

    word = ""
    for i in a:
        if i == " " or i == "\n":
            yield word
            word = ""
        else:
            word += i
    yield word


def main() -> None:
    """Точка входа"""
    string = f"Time has many faces. Time measures life, months and years. \n" \
             "Time erases mountains and creates stars. \nAnd how many things " \
             "happen between two heartbeats! \nIt is difficult to live on such " \
             "different scales of time, they tear you apart."
    for elem in generate_words(string):
        print(elem)


if __name__ == '__main__':
    main()
