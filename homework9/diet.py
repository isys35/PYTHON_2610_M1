"""
Задача 1

Диетолог работает в спортивном клубе и дает рекомендации клиентам в отношении диеты. В рамках своих рекомендаций он
запрашивает у клиентов количество граммов жиров и углеводов, которые они употребили за день. Затем на основе
приведенной ниже формулы он вычисляет количество калорий, которые получаются в результате употребления жиров. Затем
на основе еще одной формулы он вычисляет количество калорий, которые получаются в результате употребления углеводов:
Диетолог просит вас написать программу, которая выполнит эти расчеты.
"""

from homework9.decorators import diet_printer


def calculate_fat_calories(fat: int) -> int:
    """
    Функция считает количество калорий, полученных в результате употребления жиров.

    :param fat: Количество жиров
    :return: int
    """
    return fat * 9


def calculate_carbohydrates_calories(carbohydrates: int) -> int:
    """
    Функция считает количество калорий, полученных в результате употребления углеводов.

    :param carbohydrates: Количество углеводов
    :return: int
    """
    return carbohydrates * 4


@diet_printer
def calculate_calories(fat: int, carbohydrates: int) -> int:
    """
    Функция вычисляет количество калорий, употребленных в день.

    :param fat: Kоличество калорий, которые получаются в результате употребления жиров.
    :param carbohydrates: Kоличество калорий, которые получаются в результате употребления углеводов.
    :return: int
    """
    return calculate_fat_calories(fat) + calculate_carbohydrates_calories(carbohydrates)


def main() -> None:
    """ Точка входа """
    amount_of_fat = int(input("Enter the amount of fat eaten per day: "))
    amount_of_carbohydrates = int(input("Enter the amount of carbohydrates eaten per day: "))
    calculate_calories(amount_of_fat, amount_of_carbohydrates)


if __name__ == '__main__':
    main()
