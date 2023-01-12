"""
Класс с логикой в конструкторе
Напишите программу, в которой описан класс со следующими свойствами. В классе описан конструктор, которому в качестве
аргументов (помимо первой ссылки на создаваемый объект) передаются текст и целое число, причем в произвольном
порядке. Число и текст присваиваются как значения определенным полям. Если переданы два текстовых значения,
то создается только текстовое поле со значением, получающимся объединением значений аргументов. Если аргументами
переданы два числовых поля, то у объекта будет только поле с целочисленным значением, равным сумме значений
аргументов. В иных случаях поля для объекта не создаются. Создать на основе класса объекты и проверить
функциональность кода.
"""
from typing import Union


class Class_with_Logics:

    def __init__(self, arg1: Union[int, str], arg2: Union[int, str]) -> None:
        if isinstance(arg1, str) and isinstance(arg2, str) or (isinstance(arg1, int) and isinstance(arg2, int)):
            self.result = arg1 + arg2

    def get_result(self) -> Union[int, str]:
        return self.result


def main():
    try:
        concat = Class_with_Logics('Hello', ' Hello')
        print(concat.get_result())

        concat = Class_with_Logics(5, 10)
        print(concat.get_result())

        concat = Class_with_Logics(5, 'Hello')
        print(concat.get_result())
    except AttributeError as error:
        print(error)


if __name__ == '__main__':
    main()
