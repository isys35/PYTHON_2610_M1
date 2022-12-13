amount = int(input("Number of invited people: "))
if 0 < amount < 11:
    for i in range(amount):
        temp = str(input("Guest name: "))
        print(f"{temp} has been invited")
else:
    print("Too many people")
