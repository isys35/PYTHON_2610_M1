compnum = 50
r = 1
answer = int(input("Введите число :"))
if answer == compnum:
    print("Well done, you took 1 attempts")
else:
    while answer != 50:
        if answer > 50:
            answer = int(input("Верное значение меньше. Попробуйте снова :"))
            r = r + 1
        else:
            answer = int(input("Верное значение больше. Попробуйте снова :"))
            r = r + 1
print(f"Well done, you took {r} attempts")