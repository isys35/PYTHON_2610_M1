compnum = 50
number = None
attempts = 0

while number != compnum:
    number = int(input("Enter number: "))
    if number > compnum:
        print("This number is greater than expected.")
    else:
        print("This number is less than expected.")
    attempts += 1

print(f"Well done, you took {attempts} attempts.")
