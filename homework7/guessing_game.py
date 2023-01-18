"""
Задача 4

Создайте переменную с именем compnum и присвойте ей значение 50. Предложите пользователю ввести число.Пока предположение
не совпадает со значением compnum, сообщите, больше оно или меньше compnum, и предложите ввести другое число.
Если введенное значение совпадет с compnum,выведите сообщение «Well done, you took [попытки] attempts».
"""

COMPNUM = 50


def guessing(user_number: int) -> int:
    """
    Функция сравнивает переданное ей число с введенным пользователем до тех пор пока они не совпадут и подсчитывает
    количество попыток ввода числа
    :param user_number: Число введенное пользователем
    :return: Количество попыток
    """
    attempts = 1
    while user_number != COMPNUM:
        if user_number < COMPNUM:
            user_number = int(input("Ваше число меньше, введите другое число: "))
        elif user_number > COMPNUM:
            user_number = int(input("Ваше число больше, введите другое число: "))
        attempts += 1
    return attempts


def main():
    """ Точка входа"""
    user_number = int(input("Введите число: "))
    result = guessing(user_number)
    print(f"Well done,you took {result} attempts")


if __name__ == '__main__':
    main()