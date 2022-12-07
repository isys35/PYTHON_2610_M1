def generator_months(end):
    v = [
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
    for i in v[0:end]:
       yield i

f = generator_months(5)

a = f.__iter__()
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())