def repeat(count):
    def decorator(func):
        def inner(*args):
            for i in range(count):
                val = func(*args)
            return val
        return inner
    return decorator


x = 7


@repeat(count=int(input("\"7 + X = \" Enter an X: ")))
def elem():
    global x
    x += 1
    return x


if __name__ == '__main__':
    print(elem())
