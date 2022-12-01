def numbers(a):
    print(a)
    z = len(a)
    f = 0
    j = 0
    while f < z:
        if 0 == a[j] % 2:
            j = j + 1
            f = f + 1
        else:
            del a[j]
            f = f + 1
    a.sort()
    print(a)

