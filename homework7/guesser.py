"""
Задача 4

Создайте переменную с именем compnum и присвойте ей значение 50. Предложите пользователю ввести число. Пока
предположение не совпадает со значением compnum, сообщите, больше оно или меньше compnum, и предложите ввести другое
число. Если введенное значение совпадет с compnum, выведите сообщение «Well done, you took <попытки> attempts».

"""

compnum = 50


def guess_number(guess_num: int) -> int:
    """
    Функция принимает число и возвращает количество попыток за которое пользователь его угадает.

    :param guess_num: Загаданное число.
    :return: int
    """
    number = None
    attempts = 0
    while number != guess_num:
        number = int(input("Enter number: "))
        if number > guess_num:
            print("This number is greater than expected.")
        elif number < guess_num:
            print("This number is less than expected.")
        attempts += 1
    return attempts


def main() -> None:
    """ Точка входа """
    attempts = guess_number(compnum)
    print(f"Well done, you took {attempts} attempts.")


if __name__ == '__main__':
    main()
