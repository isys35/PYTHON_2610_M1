# Задача 4
# Создайте переменную с именем compnum и присвойте ей значение 50. Предложите пользователю ввести число.
# Пока предположение не совпадает со значением compnum, сообщите, больше оно или меньше compnum, и предложите
# ввести другое число. Если введенное значение совпадет с compnum,выведите сообщение «Well done,
# you took [попытки] attempts».

compnum = 50
user_number = int(input("Введите число: "))
attempts = 1
while user_number != compnum:
    if user_number < compnum:
        user_number = int(input("Ваше число меньше, введите другое число: "))
    elif user_number > compnum:
        user_number = int(input("Ваше число больше, введите другое число: "))
    attempts += 1
print(f"Well done,you took {attempts} attempts")
