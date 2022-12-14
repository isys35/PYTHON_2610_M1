"""
Спросите у пользователя, скольких людей он хочет пригласить на вечеринку. Если будет введено число меньше 10,
запросите имена и после каждого имени выведите строку «[имя] has been invited». Если введенное число больше или равно
10, выведите сообщение «Too many people».

"""


def guest_list() -> None:
    """
    Функция выводит список заданных гостей
    :return: None
    """
    amount = int(input("Number of invited people: "))
    if 0 < amount < 11:
        for i in range(amount):
            temp = str(input("Guest name: "))
            print(f"{temp} has been invited")
    else:
        print("Too many people")


def main() -> None:
    """Точка входа"""
    guest_list()


if __name__ == '__main__':
    main()
