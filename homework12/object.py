"""
Объект на основе объекта

Напишите программу, в которой описывается функция, предназначенная для создания
объекта. Объект создается на основе уже существующего объекта, который передается функции в качестве аргумента. В
создаваемый объект добавляются только те неслужебные поля из исходного объекта, которые имеют целочисленное значение.
"""
from typing import NoReturn, TypeVar

T = TypeVar("T")


class Instance:

    def __init__(self, **kwargs) -> NoReturn:
        for key, value in kwargs.items():
            setattr(self, key, value)


def factory(obj: T) -> T:
    new_dict = dict(filter(lambda item: type(item[1]) == int, obj.__dict__.items()))
    return obj.__class__(**new_dict)


def main() -> NoReturn:
    ball: Instance = Instance(size=2, color="green")
    new_ball: Instance = factory(ball)
    car: Instance = Instance(weight=3400, color="green", car_mileage=0.1)
    new_car: Instance = factory(car)
    print(new_ball.__dict__)
    print(new_car.__dict__)


if __name__ == '__main__':
    main()
