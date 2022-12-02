import time
z = int(input("Введите любое число от 1 до 12: "))
my_list = [i for i in range(1, 13)]
if z in my_list:
    for number in my_list[0:10:]:
        resalt = number * z
        print(f"{z} * {number} = {resalt}")
        time.sleep(1)
else:
    print("Нужно было ввести число от 1 до 12")