"""
Измените 3 любых прошлых домашних задач, используя конструкцию try/except

"""

compnum = 50


def guess_num() -> int:
    """
    Функция возвращает кол-во попыток угадать заданное число
    :return: int
    """
    flg = 1
    while True:
        try:
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
        except ValueError:
            print("Are you sure that the integer value? Try again")
            flg += 1


def main() -> None:
    """Точка входа"""
    print(f"Number of attempts {guess_num()}")

if __name__ == '__main__':
    main()
