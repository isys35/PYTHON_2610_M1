"""
Задача 1.

Напишите программу, в которой пользователь вводит три числа, а программа определяет, может ли существовать
треугольник со сторонами, длина которых равняется введенным значениям. Условие существования треугольника такое:
сумма двух любых (из трех введенных) чисел должна быть больше третьего числа.
"""


def triangle_check(first_meaning: float, second_meaning: float, third_meaning: float) -> bool:
    """ Функция проверяет может ли существовать треугольник
    :param first_meaning: Первая сторона треугольника
    :param second_meaning: Вторая сторона треугольника
    :param third_meaning: Третья сторона треугольника
    :return: bool
    """
    if first_meaning + second_meaning > third_meaning \
            and first_meaning + third_meaning > second_meaning \
            and second_meaning + third_meaning > first_meaning:
        return True
    return False


def main() -> None:
    """Точка входа"""
    first_meaning: float = float(input('Введите первое значение: '))
    second_meaning: float = float(input('Введите второе значение = '))
    third_meaning: float = float(input('Введите третье значение = '))
    if triangle_check(first_meaning, second_meaning, third_meaning):
        print("Ура, треугольник с такими сторонами может существовать")
    else:
        print("Увы, существование треугольника с такими сторонами невозможно")


if __name__ == '__main__':
    main()