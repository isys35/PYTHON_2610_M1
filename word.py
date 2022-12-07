a = "Код для преобразования списка Python в строку\nс помощью join():"



def generator_months(a):
    b = a.replace("\n", " ")
    r = b.split()
    for i in r:
       yield i

f = generator_months(a)

z = f.__iter__()
print(z.__next__())
print(z.__next__())
print(z.__next__())
print(z.__next__())
print(z.__next__())
print(z.__next__())
print(z.__next__())
print(z.__next__())
print(z.__next__())