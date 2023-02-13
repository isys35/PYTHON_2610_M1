def generator_months(end):
    months = [
        "Январь",
        "Февраль",
        "Март",
        "Апрель",
        "Май",
        "Июль",
        "Июль",
        "Август",
        "Сентябрь",
        "Октябрь",
        "Ноябрь",
        "Декабрь"
    ]

    for i in months[0:end]:
        yield i

if __name__ == '__main__':

    z = int(input("Введите значение от 1 до 12"  ))
    f = generator_months(z)
    for i in f:
        print(i)
        
