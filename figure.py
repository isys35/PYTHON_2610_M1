"""Описать абстрактный класс `Shape` - фигура, у которого:
- абстрактный метод `get_perimeter` (не принимает аргументов) для расчета периметра
- абстрактный метод `get_square` (не принимает аргументов) для расчета площади
Во всех дочерних классах методы `get_perimeter` и `get_square` должны возвращать
результат вычислений.
Описать класс `Circle` для круга (дочерний класс для `Shape`), у которого:
- атрибут `r` - радиус, тип `float`
- магический метод **`__init__`**, который принимает `r`
- перегрузить метод `get_perimeter` (формула длины окружности: `2 * pi * r`)
- перегрузить метод `get_square` (формула площади: `pi * r ** 2`)
Описать класс `Rectangle` для прямоугольника (дочерний класс для `Shape`), у которого:
- атрибут `a` - первая сторона, тип `float`
- атрибут `b` - вторая сторона, тип `float`
- магический метод **`__init__`**, который принимает `a` и `b`
- перегрузить метод `get_perimeter` (формула периметра: `2 * (a + b)`)
- перегрузить метод `get_square` (формула площади: `a * b`)
Описать класс `Square` для квадрата (дочерний класс для `Rectangle`), у которого:
- магический метод **`__init__`**, который принимает `a`, вызывает `super"""


from typing import Any

class Shape:

    def pi(self):
        return 3.14159265359

    def get_perimeter(self):
        raise NotImplementedError("Периметр обязательная функция")

    def get_square(self):
        raise NotImplementedError("Площадь обязательная функция")

class Circle(Shape):

    def __init__(self, r : float):
        self.r = r


    def get_perimeter(self):
        perimetr = 2 * Shape.pi(self) * self.r
        print(perimetr)

    def get_square(self):
        square = Shape.pi(self) * self.r ** 2
        print(square)

class Rectangle(Shape):

    def __init__(self, a, b : float ):
        self.a = a
        self.b = b


    def get_perimeter(self):
        perimetr = 2.0 * (self.a + self.b)
        print(perimetr)

    def get_square(self):
        square = self.a * self.b
        print(square)

class Square(Rectangle):

    def __init__(self, a):
        super()

        pass

v = Circle(24)
v.get_perimeter()
v.get_square()
z = Rectangle(6.0,8.9)
z.get_perimeter()
z.get_square()
x = Square(8)
print(x())


