user_number = int(input("Введите целое число от 1 до 12:\n "))
if user_number <= 12:
    for i in range(1, 11):
        print(i * user_number, end="\t")
else:
    print("Вы ввели число не в диапазоне от 1 до 12.")