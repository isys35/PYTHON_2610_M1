compnum = 50
shot = 1
try:
    user_num = int(input("I'm thinking of a number, name it:\n"))
    while user_num != compnum:
        if user_num < compnum:
            print("Too small")
        else:
         print("Too big")
        shot = shot + 1
        user_num = int(input("Try again:\n"))
    print("Well done, you took", shot, "attempts.")
except Exception as e:
    print("Error:", e)
finally:
    print("Good job!")