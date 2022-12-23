'''
Напишите программу, в которой пользователь вводит три числа, а программа определяет,
может ли существовать треугольник со сторонами, длина которых равняется введенным значениям.
Условие существования треугольника такое: сумма двух любых (из трех введенных)
чисел должна быть больше третьего числа.
'''


def is_triangle(first_meaning: float, second_meaning: float, third_meaning: float) -> bool:
    '''
    Функция проверяет, может ли существовать треугольник

    :param first_meaning: Первая сторона треугольника
    :param second_meaning: Вторая сторона треугольника
    :param third_meaning: Третья сторона треугольника
    :return: bool
    '''
    if first_meaning + second_meaning > third_meaning \
        and first_meaning + third_meaning > second_meaning \
        and second_meaning + third_meaning > first_meaning:
        return True
    return False


def main() -> None:
    """ Точка входа """
    first_meaning: float = float(input('первое значение = '))
    second_meaning: float = float(input('второе значение = '))
    third_meaning: float = float(input('третье значение = '))
    if is_triangle(first_meaning, second_meaning, third_meaning):
        print("Да, такой треугольник возможен")
    else:
        print("Нет, построение такого треугольника невозможно")


if __name__ == '__main__':
    main()
