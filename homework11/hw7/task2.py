"""
Предложите пользователю ввести число от 1 до 12. Выведите таблицу умножения для этого
числа.

"""


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
        a = int(input("Enter a number(1-12):"))
        if 1 <= a <= 12:
            multiplication_table(a)
            break


if __name__ == '__main__':
    main()
