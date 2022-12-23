'''Написать программу, где нужно угадать число загаданное компьютером.
На это дается 10 попыток.'''

import random


def attempts(number: int) -> None:
    """Функция принимает одно значение number, которое вводит пользователь.
        И это число сравнивает со значением компьютера и выводит угадал либо больше загаданного либо меньше.
        На это дается 10 попыток."""
    compnum = random.randint(0, 100)
    count = 0
    max_try_cunt = 10
    try_cunt = 1
    while number != compnum:
        count += 1
        if number > compnum:
            print("Число больше загаданного")
        else:
            print("Число меньше загаданного")
        if try_cunt == max_try_cunt:
            break
        number = int(input(f"Вы молодец,\nу вас осталось {max_try_cunt - try_cunt} попыток\n"))
        try_cunt += 1
    print(f"Вы угадали c {count + 1} попытки")


def main() -> None:
    user_answer = int(input("Введите число:\n"))
    attempts(user_answer)


if __name__ == '__main__':
    main()
