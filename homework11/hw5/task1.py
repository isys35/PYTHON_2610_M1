"""
Напишите программу, в которой пользователь вводит три числа, а программа определяет,
может ли существовать треугольник со сторонами, длина которых равняется введенным значениям.
Условие существования треугольника такое: сумма двух любых (из трех введенных) чисел должна
быть больше третьего числа.

 """


def existence_triangle(num1: int, num2: int, num3: int) -> bool:
    """
    Функция определяет возможность существование треугольника
    :param num1: первая сторона треугольника
    :param num2: вторая сторона треугольника
    :param num3: третья сторона треугольника
    :return: bool
    """
    if num1 + num2 > num3 and num1 + num3 > num2 and num2 + num3 > num1:
        return True
    else:
        return False


def main() -> None:
    """Точка входа"""
    print("Enter 3 numbers")
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    if existence_triangle(num1, num2, num3):
        print("Triangle with such sides exist")
    else:
        print("Triangle with such sides doesn't exist")


if __name__ == '__main__':
    main()
