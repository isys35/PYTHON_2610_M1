"""
# 18 Фигура

Описать абстрактный класс Shape - фигура, у которого:

абстрактный метод get_perimeter (не принимает аргументов) для расчета периметра
абстрактный метод get_square (не принимает аргументов) для расчета площади
Во всех дочерних классах методы get_perimeter и get_square должны возвращать
результат вычислений.

Описать класс Circle для круга (дочерний класс для Shape), у которого:

атрибут r - радиус, тип float
магический метод __init__, который принимает r
перегрузить метод get_perimeter (формула длины окружности: 2 * pi * r)
перегрузить метод get_square (формула площади: pi * r ** 2)

Описать класс Rectangle для прямоугольника (дочерний класс для Shape), у которого:

атрибут a - первая сторона, тип float
атрибут b - вторая сторона, тип float
магический метод __init__, который принимает a и b
перегрузить метод get_perimeter (формула периметра: 2 * (a + b))
перегрузить метод get_square (формула площади: a * b)
Описать класс Square для квадрата (дочерний класс для Rectangle), у которого:

магический метод __init__, который принимает a, вызывает super

"""
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):

    @staticmethod
    @abstractmethod
    def get_perimeter():
        ...

    @staticmethod
    @abstractmethod
    def get_square():
        ...


class Circle(Shape):

    def __init__(self, r):
        self.radius = r

    def get_perimeter(self):
        return 2 * pi * self.radius

    def get_square(self):
        return pi * self.radius ** 2


class Rectangle(Shape):

    def __init__(self, a, b):
        self.a_side = a
        self.b_side = b

    def get_perimeter(self):
        return 2 * (self.a_side + self.b_side)

    def get_square(self):
        return self.a_side * self.b_side


class Square(Rectangle):
    
    def __init__(self, a):
        super().__init__(a, a)


def main():
    circle = Circle(5)
    print("Circle", "\nperimeter: ", round(circle.get_perimeter(), 2))
    print("square: ", round(circle.get_square(), 2))
    rectangle = Rectangle(4, 3)
    print("Rectangle", "\nperimeter: ", round(rectangle.get_perimeter(), 2))
    print("square: ", round(rectangle.get_square(), 2))
    square = Square(8)
    print("Square: ", "\nperimeter: ", round(square.get_perimeter(), 2))
    print("square: ", round(square.get_square(), 2))


if __name__ == '__main__':
    main()