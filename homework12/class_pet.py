"""
Задача 11. Pet

Напишите класс  Pet (Домашнее животное), который должен иметь приведенные ниже атрибут данных:

__name (Для клички домашнего животного)
__animal_type (Для типа домашнего животного, например, это может быть ‘собака’)
__age (Для возраста домашнего животного)
Класс Pet должен иметь метод __init__() , который создает эти атрибуты. Он также
должен иметь приведенные ниже методы:

метод set_ name() присваивает значение полю __name;
метод set_animal_type() присваивает значение полю __animal_ type;
метод set_age*()* присваивает **значение **полю **__age;
метод get*_*name() возвращает значение поля __name;
метод get_animal_type() возвращает значение поля __animal_ type;
метод get_age() возвращает значение поля __age;
После написания данного класса напишите программу, которая создает объект класса и
предлагает пользователю ввести кличку, тип и возраст своего домашнего животного. Эти
данные должны храниться в качестве атрибутов объекта. Примените методы, чтобы извлечь имя, тип и возраст домашнего
животного и показать эти данные на экране.
"""

INPUT_NAME = input("Введите кличку домашнего питомца: ")
INPUT_TYPE = input("Введите тип домашнего питомца: ")
INPUT_AGE = input("Введите возврат питомца: ")


class Pet:

    def __init__(self):
        self.__name = ...
        self.__animal_type = ...
        self.__age = ...

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age


def main():
    """
    Точка входа
    """
    pet = Pet()
    pet.set_name(INPUT_NAME)
    pet.set_animal_type(INPUT_TYPE)
    pet.set_age(INPUT_AGE)
    print(f"Имя питомца: {pet.get_name()}\n"
          f"Тип питомца: {pet.get_animal_type()}\n"
          f"Возрат питомца: {pet.get_age()}\n")


if __name__ == '__main__':
    main()