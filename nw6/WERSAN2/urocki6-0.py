number = int(input("Ввведите число: "))

if number > 10:
    print("Число большое 10")
elif number == 5:
    print("Число равно 5")
else:
    print("не подходит")

x = 1
if x:
    y = 2
    if y:
        print("блок0")
    print("блок1")
print("блок2")


var = input("введите число: ") or input("Пожалусто введите число: ")
print(var)


