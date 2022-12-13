# number_user = int(input("Добрый день, введите число: "))
# if number_user <=12:
#    for i in range(1, 13):
#        print(f'{i} * {number_user} = {i * number_user}\t')
# else:
#    print("Введенное число больше допустимого!")

"""
Задача 2.
Предложите пользователю ввести число от 1 до 12. Выведите таблицу умножения для этого
числа.
"""


def build_multiplication_table(number: int) -> list[int]:
    """
    Функция вывода таблицы умножения
    :param number: число, на которое выводится таблица умножения
    :return: таблица умножения
    """
    return [i * number for i in range(1, 13)]


def main() -> None:
    """ Точка входа"""
    number_user = int(input("Добрый день, введите число: "))
    multiplication_table = build_multiplication_table(number_user)
    for i in range(1, 13):
        print(f'{i} * {number_user} = {i * number_user}\t')


if __name__ == '__main__':
    main()
