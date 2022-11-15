while True:
    dimen = int(input("List dimension: "))
    if dimen == 0:
        exit()
    if dimen > 0:
        break
elem = list(range(1, dimen+1))
number_dict = dict(zip(elem, reversed(elem)))

