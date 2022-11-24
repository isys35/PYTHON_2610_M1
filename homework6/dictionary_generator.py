number = int(input("Введите число: "))
keys = list(range(1, number + 1))
users_dict = dict(zip(keys, reversed(keys)))
print(keys)
print(users_dict)

