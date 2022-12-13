"""
Измените 3 любых прошлых домашних задач, используя конструкцию try/except

"""

class ValueTooLarge(Exception):
    pass


class ValueTooSmall(Exception):
    pass


def multiplication_table(a: int) -> None:
    """
    Функция выводит таблицу умножения до 10
    :param a: первый множитель
    :return: None
    """

    for i in range(1, 11):
        print(f"{a} * {i} = {a*i}")


def main() -> None:
    """Точка входа"""
    while True:
        try:
            a = int(input("Enter a number(1-12):"))
            if 1 <= a <= 12:
                multiplication_table(a)
            elif a < 1:
                raise ValueTooSmall()
            else:
                raise ValueTooLarge()
        except ValueError:
            print("Cannot convert to integer")
        except ValueTooLarge:
            print("Too large number entered")
        except ValueTooSmall:
            print("Too small number entered")


if __name__ == '__main__':
    main()
