ALL_MONTHS = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December")


def months_generator(months):
    for month in months:
        yield month


for item in months_generator(ALL_MONTHS):
    print(item)
