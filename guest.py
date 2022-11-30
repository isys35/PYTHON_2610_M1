r = 0

sum_guest = int(input("Сколько гостей Вы пригласите на вечеринку :"))
if sum_guest <= 10:
    while sum_guest != r:
        r = r + 1
        name_guest = input(f"Как зовут {r}  гостя :")
        print(f" {name_guest} has been invited")

else:
    print("Too many people")