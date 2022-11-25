class ValueTooLarge(Exception):
    pass


class ValueTooSmall(Exception):
    pass


while True:
    try:
        a = int(input("Enter a number(1-12):"))
        if 1 <= a <= 12:
            break
        elif a < 1:
            raise ValueTooSmall()
        else:
            raise ValueTooLarge()
    except ValueError:
        print("Cannot convert to integer")
    except ValueTooLarge:
        print("Too large number entered")
    except ValueTooSmall:
        print("Too small number entered")
for i in range(1, 11):
    print(f"{a} * {i} = {a*i}")
