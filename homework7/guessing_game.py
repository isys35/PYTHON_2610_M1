# compnum = 50
# shot = 1
# user_num = int(input("I'm thinking of a number, name it:\n"))
# while user_num != compnum:
#    if user_num < compnum:
#        print("Too small")
#    else:
#        print("Too big")
#    shot = shot + 1
#    user_num = int(input("Try again:\n"))
# print("Well done, you took", shot, "attempts.")

"""
Задача 4
Создайте переменную с именем compnum и присвойте ей значение 50. Предложите пользователю ввести число. Пока
предположение не совпадает со значением compnum, сообщите, больше оно или меньше compnum, и предложите ввести другое
число. Если введенное значение совпадет с compnum, выведите сообщение «Well done, you took <попытки> attempts».
"""
compnum = 50


def guess_number(guess_num: int) -> int:
    """
    Функция принимает число, сравнивает с загаданым числом и возвращает количество попыток
    :param guess_num: загаданное число
    :return: int
    """
    shot = 0
    user_num = None
    while user_num != guess_num:
        user_num = int(input("Enter number: "))
        if user_num < guess_num:
            print("Too small")
        elif user_num > guess_num:
            print("Too big")
        shot += 1
    return shot


def main() -> None:
    """Точка входа"""
    shot = guess_number(compnum)
    print(f"Well done, you took", shot, "attempts.")


if __name__ == '__main__':
    main()

