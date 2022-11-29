def executor(function, n):
    def inner(num):
        nonlocal n
        n -= 1
        if n < 0:
            return num
        return inner(function(num))

    return inner


def multiplier_x5(num):
    return num * 5


print(executor(multiplier_x5, 2)(2))
