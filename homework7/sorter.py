# from random import randint
# ready_list = []
# amount_elements = 10
#
# for i in range(amount_elements):
#    ready_list.append(randint(1, 99))
# print(ready_list)
#
# for i in range(amount_elements - 1):
#   for j in range(amount_elements - i - 1):
#        if ready_list[j] > ready_list[j + 1]:
#           ready_list[j], ready_list[j + 1] = ready_list[j + 1], ready_list[j]
#
# print(ready_list)
"""
Задача 1
Напишите программу, в которой выполняется сортировка списка (в порядке возрастания) методом пузырька. Метод такой:
последовательно сравниваются значения соседних элементов, и если значение элемента слева больше значения элемента
справа, элементы меняются местами. За один полный перебор элементов в списке элемент с самым большим значением
оказывается последим в списке. За второй перебор предпоследним оказывается элемент со вторым по величине значением и
так далее.
"""

import numpy


def bubbles_sort(ready_list) -> list:
    """
    Функция выполняет сортировку списка методом пузырька
    :param ready_list: список чисел
    :return: list
    """
    for i in range(len(ready_list) - 1, 0, -1):
        for j in range(i):
            if ready_list[j] > ready_list[j + 1]:
                ready_list[j], ready_list[j + 1] = ready_list[j + 1], ready_list[j]
    return ready_list


def main() -> None:
    """Точка входа"""
    size = int(input("Введите количество элементов: "))
    print(bubbles_sort(numpy.random.randint(0, 100, size)))


if __name__ == '__main__':
    main()
