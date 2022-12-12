"""
Задача 2

Предложите пользователю ввести число от 1 до 12. Выведите таблицу умножения для этого
числа.
"""


def build_multiplier_table(number: int) -> list[int]:
    """
    Функция делает что-то важное)))

    :param number: Какой-то важный параметр
    :return: ОЧЕНЬ-ОЧЕНЬ важный результат
    """
    return [i * number for i in range(1, 10)]


def main() -> None:
    """ Точка входа """
    number = int(input("Enter number from 1 to 12: "))
    multiplier_table = build_multiplier_table(number)
    for i in range(1, 10):
        print(f"{number} * {i} = {multiplier_table[i - 1]}")


if __name__ == '__main__':
    main()
