def print_invitations(names):
    for name in names:
        print(f"{name.title()} has been invited")


guests_number = int(input("How many people do you want to see at the party?\n"))

if 0 < guests_number < 10:
    guests = []
    while len(guests) < guests_number:
        try:
            guest = str(input("Enter a name or press Ctrl+D to finish entering: "))
        except EOFError:
            break
        guests.append(guest)
    print_invitations(guests)
elif guests_number <= 0:
    print("Congratulations! You are an introvert!")
else:
    print("Too many people!")
