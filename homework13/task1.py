"""Напишите программу, в которой описана функция, предназначенная для создания объектов.
Функции при вызове передается список и текстовый аргумент. Текстовый аргумент определяет
название класса, на основе которого создается объект. Текстовые элементы из списка
определяют названия полей объекта (нетекстовые аргументы игнорируются).
Значениями полей объекта являются натуральные числа."""

import random


def create_object(name, arr):
    meta_class = type(name, (), {})
    temp = meta_class()
    for i in arr:
        if isinstance(i, str):
            setattr(temp, i, random.randint(50, 200))
    return temp


def main():
    obj = create_object("table", ['height', 'width', 'length'])
    print(obj.__dict__)
    print(obj.__class__)


if __name__ == '__main__':
    main()
