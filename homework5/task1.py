#a = int(input("Введите число a: "))
#b = int(input("Введите число b: "))
#c = int(input("Введите число c: "))
#if a + b > c and a + c > b and b + c > a:
#   print("Треугольник существует")
#else:
#    print("Треугольник не существует")

"""
Задача 1.
Напишите программу, в которой пользователь вводит три числа, а программа определяет, может ли существовать
треугольник со сторонами, длина которых равняется введенным значениям. Условие существования треугольника такое:
сумма двух любых (из трех введенных) чисел должна быть больше третьего числа.
"""


def is_triangle(first_meaning: float, second_meaning: float, third_meaning: float) -> bool:
    """
    Функция для определения треугольника
    :param first_meaning: первое сторона
    :param second_meaning: вторая сторона
    :param third_meaning: третья сторона
    :return:
    """
    if first_meaning + second_meaning > third_meaning \
            and first_meaning + third_meaning > second_meaning \
            and second_meaning + third_meaning > first_meaning:
        return True
    return False


def main() -> None:
    """Точка входа"""
    first_meaning: float = float(input('первое значение = '))
    second_meaning: float = float(input('второе значение = '))
    third_meaning: float = float(input('третье значение = '))
    if is_triangle(first_meaning, second_meaning, third_meaning):
        print("Треугольник существует")
    else:
        print("Треугольник не существует")


if __name__ == '__main__':
    main()
