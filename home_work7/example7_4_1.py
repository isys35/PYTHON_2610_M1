compnum = 50
user_answer = int(input("Введите число:\n"))
max_try_cunt = 7
try_cunt = 1
while user_answer != compnum:
    if user_answer > compnum:
        print("Число больше загаданного")
    else:
        print("Число меньше загаданного")
    if try_cunt == max_try_cunt:
        break
    user_answer = int(input(f"Well done,\nyou took {max_try_cunt - try_cunt} attempts\n"))
    try_cunt += 1
print("Вы угадали")