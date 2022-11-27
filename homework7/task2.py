while True:
    a = int(input("Enter a number(1-12):"))
    if 1 <= a <= 12:
        break
for i in range(1, 11):
    print(f"{a} * {i} = {a*i}")
