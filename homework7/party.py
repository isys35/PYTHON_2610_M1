# num_guest = int(input("How many people do you want to invite to the party?\n"))
# if num_guest <= 10:
#    for i in range(0, num_guest):
#        name_guest = input("Enter name: ")
#        print(name_guest, "has been invited.")
# else:
#    print("Too many people")
"""
Задача 3
Спросите у пользователя, скольких людей он хочет пригласить на вечеринку. Если будет введено число меньше 10,
запросите имена и после каждого имени выведите строку «[имя] has been invited». Если введенное число больше или равно
10, выведите сообщение «Too many people».
"""


def send_invitation(guests: list[str]) -> list[str]:
    """
    Функция генерирует приглашения для гостей на вечеринку.
    :param guests: количество гостей
    :return: list[str]
    """
    return [f"{guest.title()} has been invited." for guest in guests]


def main() -> None:
    """Точка входа"""
    num_guest: int = int(input("How many people do you want to invite to the party?\n"))
    if 0 < num_guest < 10:
        guests = []
        while len(guests) < num_guest:
            guest = str(input("Enter name: "))
            guests.append(guest)
        invitations: list[str] = send_invitation(guests)
        for invitation in invitations:
            print(invitation)
    else:
        print("Too many people")


if __name__ == '__main__':
    main()
