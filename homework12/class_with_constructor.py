"""
Задача 6 Класс с конструктором

Напишите программу, в которой описывается класс со следующими характеристиками. У класса есть конструктор, которому
(кроме ссылки на объект вызова) передаются два значения. Эти значения присваиваются полям объекта класса. В классе
должен быть описан метод, при вызове которого отображаются значения полей класса. Проверьте функциональность класса,
создав на его основе несколько объектов.
"""


class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_user(self):
        return self.name, self.age


if __name__ == '__main__':
    user_one = User("Вася", 31)
    user_two = User("Игнат", 25)
    print(f"{user_one.get_user()}\n{user_two.get_user()}")