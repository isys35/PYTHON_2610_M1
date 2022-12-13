"""
Создайте программу, которая запрашивает у пользователя два целых числа a и b, после чего выводит
на экран результаты математических операций.

"""


def calculate(num1: int, num2: int) -> None:
    """
    Функция выполняет математические операции

    :param num1: первое число
    :param num2: второе число
    :return: None
    """
    print("Sum:", num1 + num2, "\nDifference:", num1 - num2, "\nProduct:", num1 * num2)
    print("Quotient of:", num1 / num2, "\nModulo:", num1 % num2, "\nA to the B power:", num1 ** num2)


def main() -> None:
    """Точка входа"""
    print("Enter 2 numbers")
    num1 = int(input())
    num2 = int(input())
    calculate(num1, num2)


if __name__ == '__main__':
    main()
