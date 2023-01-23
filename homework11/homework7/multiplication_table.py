"""
Задача 2

Предложите пользователю ввести число от 1 до 12. Выведите таблицу умножения для этого числа.
"""


def calculate(number: int) -> list[int]:
    """
    Функция возвращает произведение переданного ей числа на числа от 0 до 9
    :param number: Число введенное пользователем
    :return: Список чисел
    """
    return [i * number for i in range(0, 9)]


def main():
    """Точка входа"""
    user_number = int(input("Введите число от 1 до 12: "))
    total_table = calculate(user_number)
    number = 0
    for item in total_table:
        print(f"{number} x {user_number} = {item}")
        number += 1


if __name__ == '__main__':
    main()