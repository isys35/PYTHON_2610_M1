'''Напишите программу, в которой используется функция-генератор,
создающая итерируемый объект с названиями месяцев'''

MONTHS = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль",
          "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]


def months_generator(months):
    for month in months:
        yield month


def main() -> None:
    for item in months_generator(MONTHS):
        print(item, end=", ")


if __name__ == '__main__':
    main()
