def func2(func1, n):
    for i in range(n):
        func1()
    return func2


if __name__ == '__main__':
    def func3():
        print("Hello")
    func2(func3, 5)


# def get(func, n):
#     def inner():
#         for _ in range(n):
#             func()
#     return inner
