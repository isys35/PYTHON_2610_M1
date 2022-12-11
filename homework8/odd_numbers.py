"""
Задача 2

Напишите программу с функцией, аргументом, которой передается
числовой список, а результатом является еще один список, в который
включены только нечетные числа из списка-аргумента.
"""


def get_odd_numbers(list_of_numbers: list[int]) -> list[int]:
    """
    Функция отфильтровывает нечетные числа из входящего списка.

    :param list_of_numbers: Список чисел
    :return: list[int]
    """
    return list(filter(lambda x: (x % 2 == 1), list_of_numbers))


def main() -> None:
    """ Точка входа """
    list_of_numbers = [1, 6, 8, 7, 66, 89]
    print(get_odd_numbers(list_of_numbers))


if __name__ == '__main__':
    main()
