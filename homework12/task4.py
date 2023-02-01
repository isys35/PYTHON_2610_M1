"""Напишите класс `Pet` (Домашнее животное), который должен иметь приведенные ниже атрибут данных:

- `__name` (Для клички домашнего животного)
- `__animal_type` (Для типа домашнего животного, например, это может быть ‘собака’)
- `__age` (Для возраста домашнего животного)

Класс `Pet` должен иметь метод `__init__()`, который создает эти атрибуты. Он также
должен иметь приведенные ниже методы:

- метод `set_name()` присваивает значение полю `__name`;
- метод `set_animal_type()` присваивает значение полю `__animal_ type`;
- метод `set_age()` присваивает значение полю `__age`;
- метод `get_name()` возвращает значение поля `__name`;
- метод `get_animal_type()` возвращает значение поля `__animal_ type`;
- метод `get_age()` возвращает значение поля `__age`;

После написания данного класса напишите программу, которая создает объект класса и
предлагает пользователю ввести кличку, тип и возраст своего домашнего животного. Эти
данные должны храниться в качестве атрибутов объекта. Примените методы, чтобы извлечь имя, тип и
возраст домашнего животного и показать эти данные на экране."""


class Pet:
    def __init__(self):
        self.__name: str = ""
        self.__animal_type: str = ""
        self.__age: int = 0

    def set_name(self, name: str):
        self.__name = name

    def set_animal_type(self, animal_type: str):
        self.__animal_type = animal_type

    def set_age(self, age: int):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age


def main():
    pet = Pet()
    name = str(input("Pet's name:"))
    animal_type = str(input("Pet's type:"))
    while True:
        try:
            age = int(input("Pet's age: "))
        except ValueError:
            print("Invalid value")
        else:
            break
    pet.set_name(name)
    pet.set_animal_type(animal_type)
    pet.set_age(age)
    print(f"Pet's name: {pet.get_name()}")
    print(f"Pet's type: {pet.get_animal_type()}")
    print(f"Pet's age: {pet.get_age()} ")


if __name__ == '__main__':
    main()
