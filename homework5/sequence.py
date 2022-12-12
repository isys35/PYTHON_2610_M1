"""
Задача 2

Напишите программу, в которой пользователь вводит три целых числа, а программа проверяет, являются ли эти числа тремя
последовательными элементами арифметической последовательности. В арифметической последовательности каждый новый член
получается прибавлением к предыдущему определенного фиксированного числа.
"""


def check_sequence(first_meaning: int, second_meaning: int, third_meaning: int) -> bool:
    """
    Функция проверяет, являются ли эти числа тремя последовательными элементами арифметической последовательности

    :param first_meaning: Первое число
    :param second_meaning: Второе число
    :param third_meaning: Третье число
    :return: bool
    """
    if (first_meaning + third_meaning) / 2 * 3 == (first_meaning + second_meaning + third_meaning):
        return True
    return False


def main() -> None:
    """ Точка входа """
    first_meaning: int = int(input("Введите число a: "))
    second_meaning: int = int(input("Введите число b: "))
    third_meaning: int = int(input("Введите число c: "))
    if check_sequence(first_meaning, second_meaning, third_meaning):
        print("\nЭто арифметическая последовательность.")
    else:
        print("\nЭто НЕ арифметическая последовательность")


if __name__ == '__main__':
    main()
