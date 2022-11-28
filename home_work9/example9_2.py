def double(function):
    def inner(argument):
        return function(function(argument))
    return inner


def multiply_by_two(x):
    return x * 2


if __name__ == '__main__':
    try:
        n = int(input("Введите число: "))
        print(double(multiply_by_two)(n))
    except Exception:
        print("Что-то пошло не так.\nПопробуйте снова.")
