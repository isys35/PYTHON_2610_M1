"""
Задача 10 Объект на основе объекта

Напишите программу, в которой описывается функция, предназначенная для создания объекта.
Объект создается на основе уже существующего объекта, который передается функции в качестве аргумента.
В создаваемый объект добавляются только те неслужебные поля из исходного объекта, которые имеют целочисленное значение.
"""


class MyObject:

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self.__setattr__(key, value)


def object_on_object(obj):
    param = {key: value for key, value in obj.__dict__.items() if type(value) == int}
    return obj.__class__(**param)


def main():
    """ Точка входа"""
    object_one = MyObject(name="Siarhei", age=31, vocation="developer", height=182.4)
    print(object_one.__dict__)
    object_two = object_on_object(object_one)
    print(object_two.__dict__)


if __name__ == '__main__':
    main()