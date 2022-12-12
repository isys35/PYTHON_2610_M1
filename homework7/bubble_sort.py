"""
Задача 1

Напишите программу, в которой выполняется сортировка списка (в порядке возрастания) методом пузырька. Метод такой:
последовательно сравниваются значения соседних элементов, и если значение элемента слева больше значения элемента
справа, элементы меняются местами. За один полный перебор элементов в списке элемент с самым большим значением
оказывается последим в списке. За второй перебор предпоследним оказывается элемент со вторым по величине значением и
так далее.

"""

import numpy


def bubble_sort(numbers_list: list) -> list:
    """
    Функция выполняет сортировку списка методом пузырька.

    :param numbers_list: Список чисел
    :return: list
    """
    for i in range(len(numbers_list) - 1, 0, -1):
        for j in range(i):
            if numbers_list[j] > numbers_list[j + 1]:
                numbers_list[j], numbers_list[j + 1] = numbers_list[j + 1], numbers_list[j]
    return numbers_list


def main() -> None:
    """ Точка входа """
    size = int(input("Enter list size: "))
    print(bubble_sort(numpy.random.randint(0, 100, size)))


if __name__ == '__main__':
    main()
