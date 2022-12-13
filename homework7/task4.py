compnum = 50
flg = 1
while True:
    x = int(input("Enter a number: "))
    if x > 50:
        print(f"Hidden number is less than {x}")
        flg += 1
    elif x < 50:
        print(f"Hidden number is largest than {x}")
        flg += 1
    else:
        print("You guessed it")
        print(f"Number of attempts {flg}")
        break
