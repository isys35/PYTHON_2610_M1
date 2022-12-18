# a = int(input("Введите число от 1 до 7: "))
# if a == 1:
#    print("Понедельник")
# elif a == 2:
#    print("Вторник")
# elif a == 3:
#    print("Среда")
# elif a == 4:
#   print("Четверг")
# elif a == 5:
#    print("Пятница")
# elif a == 6:
#    print("Суббота")
# else:
#   print("Воскресенье")

"""
Задача 3.
Напишите программу, в которой пользователь вводит целое число от 1 до 7 включительно, а программа выводит название дня
недели, соответствующее этому числу ("Понедельник" для 1, "Вторник" для 2, и так далее).
"""
DAY = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
WEEK: dict[int, DAY] = {
    1: "Понедельник",
    2: "Вторник",
    3: "Среда",
    4: "Четверг",
    5: "Пятница",
    6: "Суббота",
    7: "Воскресенье"
}


def find_out_the_day(number: int) -> DAY:
    """
    Функция, определяющая день недели по заданному числу
    :param number: номер дня недели
    :return: DAY
    """
    return WEEK[number]


def main() -> None:
    """Точка входа"""
    number: int = int(input("Введите число от 1 до 7: "))
    print(find_out_the_day(number))


if __name__ == '__main__':
    main()
