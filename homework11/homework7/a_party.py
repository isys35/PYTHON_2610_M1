"""
Задача 3

Спросите у пользователя, скольких людей он хочет пригласить на вечеринку. Если будет введено число меньше 10,
запросите имена и после каждого имени выведите строку «[имя] has been invited». Если введенное число больше или
равно 10, выведите сообщение «Too many people».
"""


def guest_add(count: int) -> dict:
    """
    Функция генерирует словарь с порядковым номерами и именами гостей на основании переданного ей числового аргумента
    :param count: Количество гостей
    :return: Словарь с именами гостей
    """
    list_guest = [i + 1 for i in range(0, count)]
    dict_guest = dict.fromkeys(list_guest)
    number_guest = 1
    for guest in list_guest:
        name_guest = input(f"Введите имя гостя №{number_guest}: ")
        print(f"{name_guest} has been invited")
        dict_guest[number_guest] = name_guest
        number_guest += 1
    return dict_guest


def guest_print(guests: dict[int, str]) -> None:
    """
    Функция прнимает список гостей и выводит на печать
    :param guests: Список гостей
    :return: None
    """
    print("Список гостей:")
    for key, value in guests.items():
        print(f"Гость {key}: {value}")


def main():
    """ Точка входа"""
    try:
        amount_guest = int(input("Сколько гостей планируется на вечеринке? "))
        if amount_guest < 10:
            guests = guest_add(amount_guest)
            guest_print(guests)
        elif amount_guest > 10:
            print("Too many people!")
    except ValueError:
        print("Введенное значение не является числом")


if __name__ == '__main__':
    main()
