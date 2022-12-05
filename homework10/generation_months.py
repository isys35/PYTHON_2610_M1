MONTHS = ("Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
          "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь")


def generation_months(months):
    for month in months:
        yield month


for item in generation_months(MONTHS):
    print(item)
