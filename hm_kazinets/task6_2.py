num = int(input("Введите число: "))
list_user = [i for i in range(1, num + 1)]
result = dict(zip(list_user, reversed(list_user)))
print(result)
