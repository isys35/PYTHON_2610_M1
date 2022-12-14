"""
Напишите программу с функцией, которая аргументами получает ссылку
на функцию и целое число. Результатом которой является n-кратное
исполнение переданной функции.

"""


def repeat(count):
    """
    Функция-декоратор изменяет кол-во повторений функции
    :param count: кол-во повторений
    :return: Callable[[int], None]
    """
    def decorator(func):
        def inner(*args):
            for i in range(count):
                val = func(*args)
            return val
        return inner
    return decorator


x = 7


@repeat(count=int(input("\"7 + X = \" Enter an X: ")))
def elem() -> int:
    global x
    x += 1
    return x


def main() -> None:
    print(elem())


if __name__ == '__main__':
    main()
