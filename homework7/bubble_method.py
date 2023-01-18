"""
Задача 1

Напишите программу, в которой выполняется сортировка списка (в порядке возрастания) методом пузырька. Метод такой:
последовательно сравниваются значения соседних элементов, и если значение элемента слева больше значения элемента справа,
элементы меняются местами. За один полный перебор элементов в списке элемент с самым большим значением оказывается последим
в списке. За второй перебор предпоследним оказывается элемент со вторым по величине значением и так далее.
"""

from random import randint


def bubble_sort(count: int) -> list:
    """
    Функция генерирует и выполняет сортировку списка методом пузырька
    :param count: Количество элементов списка
    :return: Отсортированный список
    """
    num_list: list = [randint(1, 50) for i in range(count)]
    print(num_list)
    for i in range(len(num_list) - 1):
        for j in range(len(num_list) - 1 - i):
            if num_list[j] > num_list[j + 1]:
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]
    return num_list


def main():
    """ Точка входа"""
    len_list = int(input("Введите число от 1 до 50: "))
    result = bubble_sort(len_list)
    print(result)


if __name__ == '__main__':
    main()