z = int(input("Введите любое число: ")) + 1
a = [i for i in range(1,z)]
print(a)
b = sorted(a, reverse=True)
print(b)
dic = dict(zip(a, b))
print(dic)