number_user = int(input("Добрый день, введите число: "))
if number_user <=12:
    for i in range(1, 13):
        print(f'{i} * {number_user} = {i * number_user}\t')
else:
    print("Введенное число больше допустимого!")
