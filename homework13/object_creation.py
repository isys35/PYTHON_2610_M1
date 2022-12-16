"""
Функция для создания объектов

Напишите программу, в которой описана функция, предназначенная для создания объектов.
Функции при вызове передается список и текстовый аргумент. Текстовый аргумент определяет название класса,
на основе которого создается объект. Текстовые элементы из списка определяют названия полей объекта (нетекстовые
аргументы игнорируются). Значениями полей объекта являются натуральные числа.
"""

import random
from typing import List, NoReturn


def make_object(name: str, attributes: List) -> object:
    meta_class = type(name, (), {})
    temp_object: object = meta_class()
    for key in attributes:
        if isinstance(key, str):
            setattr(temp_object, key, random.randint(1, 1000))
    return temp_object


def main() -> NoReturn:
    ball = make_object("Ball", ["weight", "size", 5])
    print(ball.__dict__)
    print(ball.__class__)


if __name__ == '__main__':
    main()
