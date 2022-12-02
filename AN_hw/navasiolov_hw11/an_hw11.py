"""
Задача 1.

Напишите программу, в которой пользователь
вводит три числа, а программа определяет,
может ли существовать треугольник со
сторонами, длина которых равняется введенным
значениям. Условие существования треугольника такое:
сумма двух любых (из трех введенных) чисел должна
быть больше третьего числа.
"""

def is_triangle(side_1: int, side_2: int, side_3: int) -> bool:
    """
        Функция проверяет, может ли существовать треугольник

    :param side_1: Сторона А
    :param side_2: Сторона Б
    :param side_3: Сторона Ц
    :return: bool
    """
    if side_1 + side_2 > side_3:
        return True
    return False
    if side_2 + side_3 > side_1:
        return True
    return False
    if side_3 + side_1 > side_2:
        return True
    return False

def main() -> is_triangle:
    """ Точка входа """
    side_1: int = int(input("\n--> Сторона А: "))
    side_2: int = int(input("--> Сторона Б: "))
    side_3: int = int(input("--> Сторона Ц: "))
    if is_triangle(side_1, side_2, side_3):
        print("Да, такой треугольник возможен")
    else:
        print("Нет, построение такого треугольника невозможно")

if __name__ == "__main__":
    main()




  # Предыдущий вариант
#print("\n!Создайте Треугольник!")
#side_1 = int(input("\n--> Сторона А: "))
#side_2 = int(input("--> Сторона Б: "))
#side_3 = int(input("--> Сторона Ц: "))
#if side_1 + side_2 > side_3:
    #print(" Треугольник ")
#else:
    #print(" Пока не ")
#if side_2 + side_3 > side_1:
    #print(" Этот")
#else:
    #print(" Не ")
#if side_3 + side_1 > side_2:
    #print(" Существует")
#else:
    #print(" Не доработан! ")
