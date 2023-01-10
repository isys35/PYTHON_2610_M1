"""
Класс с конструктором
Напишите программу, в которой описывается класс со следующими характеристиками. У класса
есть конструктор, которому (кроме ссылки на объект вызова) передаются два значения. Эти значения присваиваются полям
объекта класса. В классе должен быть описан метод, при вызове которого отображаются значения полей класса. Проверьте
функциональность класса, создав на его основе несколько объектов.
"""


class Person:
    def __init__(self, name: str, company: str, age=23) -> None:
        self.__age = age
        self.__name = name
        self.__company = company

    def set_age(self, age: int) -> None:
        if 1 <= age <= 120:
            self.__age = age
        else:
            print('Ne verno')

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name

    def get_company(self):
        return self.__company

    def display_info(self):
        print(f'Name: {self.__name}, Age: {self.__age}, Company: {self.__company}.')


def main() -> None:
    tom = Person('Tom', 'Microsoft', 30)
    tom.display_info()
    bob = Person('Bob', 'Apple')
    bob.display_info()


if __name__ == '__main__':
    main()
