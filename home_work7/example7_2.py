user_number = int(input("Введите целое число от 1 до 12:\n "))
number = 1
if user_number <= 12:
    while number <= 10:
        print(user_number * number, end="\t")
        number += 1
else:
    print("Вы ввели число не в диапазоне от 1 до 12.")