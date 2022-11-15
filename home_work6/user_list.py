user_number = int(input("Введите целое неотрицательное число:\n"))
user_list = list(range(1, user_number + 1))
user_dict = dict(zip(user_list, reversed(user_list)))
print(user_list, user_dict)