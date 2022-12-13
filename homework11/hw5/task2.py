"""
Напишите программу, в которой пользователь вводит три целых числа, а программа проверяет, являются ли эти числа тремя
последовательными элементами арифметической последовательности. В арифметической последовательности каждый новый член
получается прибавлением к предыдущему определенного фиксированного числа.

"""


def check_sequence(a1: int, a2: int, a3: int) -> bool:
    """
    Функция проверяет возможность существования арифметической прогрессии
    :param a1: первое число прогрессии
    :param a2: второе число прогрессии
    :param a3: третье число прогрессии
    :return: bool
    """
    if a2 == (a1+a3)/2:
        print("This sequence is an arithmetic progression")
    else:
        print("This sequence isn't an arithmetic progression")


def main() -> None:
    """Точка входа"""
    print("Enter 3 numbers")
    a1 = int(input())
    a2 = int(input())
    a3 = int(input())
    check_sequence(a1, a2,  a3)

if __name__ == '__main__':
    main()
