"""
Задача 1

Измените 3 любых прошлых домашних задач, ипользуя контсрукцию try/except
"""

from typing import NoReturn


def calculate(a: int, b: int) -> NoReturn:
    """
    Функция выполняет математические операции

    :param a: Первое число
    :param b: Второе число
    :return: NoReturn
    """
    print("Сумма чисел a и b равна: ", a + b)
    print("Разность чисел a и b равна: ", a - b)
    print("Произведение чисел a и b равно: ", a * b)
    print("Частное от деления чисел a и b равно: ", a / b)
    print("Остаток от деления числа a на число b равен: ", a % b)
    print("Число a  в степени b равно: ", a ** b)


def main() -> None:
    """ Точка входа """
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    try:
        calculate(a, b)
    except ZeroDivisionError:
        print("ОШИБКА!!! Попытка деления на ноль")
    except ValueError:
        print("ОШИБКА!!! Неверный ввод данных")
    except Exception as err:
        print(f"Что-то пошло не так: {err}")


if __name__ == '__main__':
    main()
