"""
Функция для создания объектов
Напишите программу, в которой описана функция, предназначенная для создания объектов.
Функции при вызове передается список и текстовый аргумент. Текстовый аргумент определяет название класса,
на основе которого создается объект. Текстовые элементы из списка определяют названия полей объекта (нетекстовые
аргументы игнорируются). Значениями полей объекта являются натуральные числа.
"""

import random
from typing import List


def make_object(name: str, attributes: List) -> object:
    meta_class = type(name, (), {})
    temp_object: object = meta_class()
    for key in attributes:
        if isinstance(key, str):
            setattr(temp_object, key, random.randint(1, 10))
    return temp_object


def main() -> None:
    box = make_object("Box", ['height', 'width', 'length', 1, 2, 3, 4])
    print(box.__dict__)
    print(box.__class__)


if __name__ == '__main__':
    main()
