"""
# 7 Класс с логикой в конструкторе

Напишите программу, в которой описан класс со следующими свойствами. В классе описан конструктор, которому в качестве
аргументов (помимо первой ссылки на создаваемый объект) передаются текст и целое число, причем в произвольном порядке.
Число и текст присваиваются как значения определенным полям. Если переданы два текстовых
значения, то создается только текстовое поле со значением, получающимся объединением значений аргументов.
Если аргументами переданы два числовых поля, то у объекта будет только поле с целочисленным значением, равным сумме
значений аргументов. В иных случаях поля для объекта не создаются. Создать на основе класса объекты и проверить
функциональность кода.
"""


class ConstructorWithLogic:
    def __init__(self, var_1, var_2):
        if isinstance(var_1, str) and isinstance(var_2, str) or (isinstance(var_1, int) and isinstance(var_2, int)):
            self.result = var_1 + var_2

    def get_result(self):
        return self.result


def main() -> None:
    try:
        test_1 = ConstructorWithLogic("Здравствуйте ", "Дмитрий")
        print(test_1.get_result())

        test_2 = ConstructorWithLogic(1, 2)
        print(test_2.get_result())

        test_3 = ConstructorWithLogic("Здравствуйте ", 1)
        print(test_3.get_result())

    except AttributeError:
        print("Error!")


if __name__ == '__main__':
    main()
