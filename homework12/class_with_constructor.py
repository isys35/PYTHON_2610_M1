"""
# 6 Класс с конструктором

Напишите программу, в которой описывается класс со следующими характеристиками. У класса есть конструктор,
которому (кроме ссылки на объект вызова) передаются два значения. Эти значения присваиваются полям объекта класса.
В классе должен быть описан метод, при вызове которого отображаются значения полей класса. Проверьте функциональность
класса, создав на его основе несколько объектов.
"""

class CheckIn:
    def __init__(self, surname, flight_num):
        self.surname = surname
        self.flight_num = flight_num

    def print_check_in(self):
        print(f"{self.surname} зарегистрирован на рейс № {self.flight_num}")


if __name__ == '__main__':
    passenger_1 = CheckIn("Петров", 7215)
    passenger_2 = CheckIn("Сидоров", 7251)
    passenger_1.print_check_in()
    passenger_2.print_check_in()
