compnum = 50
count = 1
user_answer = int(input("Введите число:\n"))
while user_answer != compnum:
    count += 1
    if user_answer > compnum:
        print("Число больше загаданного")
    else:
        print("Число меньше загаданного")
    user_answer = int(input(f"Well done,\nyou took {count} attempts\n"))
print("Вы угадали")


