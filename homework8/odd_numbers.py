"""
Задача 2

Напишите программу с функцией, аргументом которой передается числовой список, а результатом является еще один список,в
который включены только нечетные числа из списка-аргумента.
"""

from random import randint


def odd_numbers(test_list: list[int]) -> list[int]:
    """
    Функция принимает список числовых аргументов и возвращает только нечетные значения
    :param test_list: Список числовых аргументов
    :return: Список с нечетными значениями
    """
    result_list = []
    for i in test_list:
        if i % 2 != 0:
            result_list.append(i)
    return result_list


def main():
    """Точка входа"""
    num_list = [randint(0, 100) for i in range(10)]
    print(num_list)
    print(odd_numbers(num_list))


if __name__ == '__main__':
    main()