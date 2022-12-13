MONTHS = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль",
              "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]


def months_generator(months):
    for month in months:
        yield month


if __name__ == '__main__':
    for item in months_generator(MONTHS):
        print(item, end=", ")
