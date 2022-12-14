"""
Напишите программу с функцией, аргументом которой передается
числовой список, а результатом является еще один список, в который
включены только нечетные числа из списка-аргумента.
"""


def odd_num(arr: list) -> list[int]:
    """
    Функция создает список из нечетных элементов другого списка
    :param arr: список аргуметнов
    :return: list
    """
    return [i for i in arr if i % 2 != 0]


def main() -> None:
    """Точка входа"""
    list_1 = []
    print("Enter a sequence of numbers(!letter)")
    while True:
        try:
            tmp = int(input())
            list_1.append(tmp)
        except ValueError:
            print("Enter a letter; recording a list completed")
            break
    new_list = odd_num(list_1)
    print("The first list", list_1)
    print("Odd numbers in list:", new_list)


if __name__ == '__main__':
    main()
