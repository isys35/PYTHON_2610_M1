"""
Задача 3

Спросите у пользователя, скольких людей он хочет пригласить на вечеринку. Если будет введено число меньше 10,
запросите имена и после каждого имени выведите строку «[имя] has been invited». Если введенное число больше или равно
10, выведите сообщение «Too many people».
"""


def build_invitations(guests: list[str]) -> list[str]:
    """
    Функция генерирует приглашения для гостей.

    :param guests: Количество гостей
    :return: list[str]
    """
    return [f"{guest.title()} has been invited." for guest in guests]


def main() -> None:
    """ Точка входа """
    try:
        guests_number: int = int(input("How many people do you want to see at the party?\n"))
        if 0 < guests_number < 10:
            guests = []
            while len(guests) < guests_number:
                try:
                    guest = str(input("Enter a name or press Ctrl+D to finish entering: "))
                except EOFError:
                    break
                guests.append(guest)
            invitations: list[str] = build_invitations(guests)
            for invitation in invitations:
                print(invitation)
        elif guests_number <= 0:
            raise ValueError("Congratulations! You are an introvert!")
        else:
            raise ValueError("Too many people!")

    except Exception as err:
        print(f"Something went wrong: {err}")


if __name__ == '__main__':
    main()
