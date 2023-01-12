"""
Напишите программу, в которой описывается функция, предназначенная для создания объекта. Объект создается на основе
уже существующего объекта, который передается функции в качестве аргумента. В создаваемый объект добавляются только
те неслужебные поля из исходного объекта, которые имеют целочисленное значение.
"""


from typing import TypeVar

New = TypeVar("New")


class Instance:

    def __init__(self, **kwargs) -> None:
        for key, value in kwargs.items():
            setattr(self, key, value)


def factory(obj: New) -> New:
    new_dict = {key: value for key, value in obj.__dict__.items() if isinstance(value, int)}
    return obj.__class__(**new_dict)


def main() -> None:
    box: Instance = Instance(size=5)
    new_box: Instance = factory(box)
    phone: Instance = Instance(diagonal=6, price=1000)
    new_phone: Instance = factory(phone)
    print(new_box.__dict__)
    print(new_phone.__dict__)


if __name__ == '__main__':
    main()
