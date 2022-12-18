"""
Задача 2.

Напишите программу с функцией, которая аргументами получает ссылку на функцию и целое число.
Результатом которой является n-кратное исполнение переданной функции
"""

def func2(func1, n):
    """
    Функция, результатом которой является исполнение функции.
    :param func1: передаваемая функция
    :param n: число повторений
    :return: func2
    """
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
