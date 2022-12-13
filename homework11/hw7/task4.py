"""
Создайте переменную с именем compnum и присвойте ей значение 50. Предложите пользователю ввести число. Пока
предположение не совпадает со значением compnum, сообщите, больше оно или меньше compnum, и предложите ввести другое
число. Если введенное значение совпадет с compnum, выведите сообщение «Well done, you took <попытки> attempts».

"""

compnum = 50


def guess_num() -> int:
    """
    Функция возвращает кол-во попыток угадать заданное число
    :return: int
    """
    flg = 1
    while True:
        x = int(input("Enter a number: "))
        if x > 50:
            print(f"Hidden number is less than {x}")
            flg += 1
        elif x < 50:
            print(f"Hidden number is largest than {x}")
            flg += 1
        else:
            print("You guessed it")
            return flg


def main():
    """Точка входа"""
    print(f"Number of attempts {guess_num()}")


if __name__ == '__main__':
    main()