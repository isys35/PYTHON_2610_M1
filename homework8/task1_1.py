
try:
    number_user = int(input("Добрый день, введите число от 1 до 12: "))
    if number_user <= 12:
        for i in range(1, 13):
            print(f'{i} * {number_user} = {i * number_user}\t')
    else:
        print("Введенное число больше допустимого!")
except ValueError:
    print("Error: You did not enter a number")
finally:
    print("Досвидания")
