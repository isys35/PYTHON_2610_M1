num_guest = int(input("How many people do you want to invite to the party?\n"))
if num_guest <= 10:
    for i in range(0, num_guest):
        name_guest = input("Enter name: ")
        print(name_guest, "has been invited.")
else:
    print("Too many people")
