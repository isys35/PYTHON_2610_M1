"""
Напишите программу, в которой пользователь вводит целое число от 1 до 7 включительно,
а программа выводит название дня недели, соответствующее этому числу ("Понедельник"
для 1, "Вторник" для 2, и так далее).

"""


def weeks() -> None:
    """
    Функция выводит день недели
    :return: None
    """
    print({"1": "Monday",
           "2": "Tuesday",
           "3": "Wednesday",
           "4": "Thursday",
           "5": "Friday",
           "6": "Saturday",
           "7": "Sunday"
           }[input("Enter the number: ")])


def main() -> None:
    weeks()


if __name__ == '__main__':
    main()
