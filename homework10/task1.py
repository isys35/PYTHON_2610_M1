def generate_months(tup):
    for i in tup:
        yield i


if __name__ == '__main__':
    months = ("January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December")
    for elem in generate_months(months):
        print(elem)
