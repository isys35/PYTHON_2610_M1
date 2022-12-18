"""
18 Фигура
Описать абстрактный класс Shape - фигура, у которого:
абстрактный метод get_perimeter (не принимает аргументов) для расчета периметра,
абстрактный метод get_square (не принимает аргументов) для расчета площади,
Во всех дочерних классах методы get_perimeter и get_square должны возвращать результат вычислений.

Описать класс Circle для круга (дочерний класс для Shape), у которого:
атрибут r - радиус, тип float, магический метод __init__, который принимает r
перегрузить метод get_perimeter (формула длины окружности: 2 * pi * r)
перегрузить метод get_square (формула площади: pi * r ** 2)

Описать класс Rectangle для прямоугольника (дочерний класс для Shape), у которого:
атрибут a - первая сторона, тип float, атрибут b - вторая сторона, тип float
магический метод __init__, который принимает a и b, перегрузить метод get_perimeter (формула периметра: 2 * (a + b))
перегрузить метод get_square (формула площади: a * b).

Описать класс Square для квадрата (дочерний класс для Rectangle), у которого:
магический метод __init__, который принимает a, вызывает super
"""
import math
from abc import ABC, abstractmethod
from typing import NoReturn

PI = math.pi


class Shape(ABC):

    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def get_square(self):
        pass


class Circle(Shape):

    def __init__(self, r: float) -> NoReturn:
        self.radius = r

    def get_perimeter(self) -> float:
        return 2 * PI * self.radius

    def get_square(self) -> float:
        return PI * self.radius ** 2


class Rectangle(Shape):

    def __init__(self, a: float, b: float) -> NoReturn:
        self.first_side = a
        self.second_side = b

    def get_perimeter(self) -> float:
        return 2 * (self.first_side + self.second_side)

    def get_square(self) -> float:
        return self.first_side * self.second_side


class Square(Rectangle):

    def __init__(self, a: float) -> NoReturn:
        super().__init__(a, a)


def main() -> NoReturn:
    circle = Circle(3)
    print(circle.get_perimeter())
    print(circle.get_square())

    rectangle = Rectangle(2, 3)
    print(rectangle.get_perimeter())
    print(rectangle.get_square())

    square = Square(2)
    print(square.get_perimeter())
    print(square.get_square())


if __name__ == '__main__':
    main()
