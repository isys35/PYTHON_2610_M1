"""
Напишите программу, в которой используется функция-генератор,
создающая итерируемый объект с названиями месяцев
"""


def generate_months(tup: tuple) -> str:
    """
    Функция, создающая итерируемый объект
    :param tup: кортеж для итерации
    :return: str
    """
    for i in tup:
        yield i


def main() -> None:
    months = ("January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December")
    for elem in generate_months(months):
        print(elem)


if __name__ == '__main__':
    main()
