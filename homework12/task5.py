"""Напишите программу, в которой описывается функция, предназначенная для создания объекта.
Объект создается на основе уже существующего объекта, который передается функции в качестве
аргумента. В создаваемый объект добавляются только те неслужебные поля из исходного объекта,
которые имеют целочисленное значение."""


class Some:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self.__setattr__(key, value)


def create_object(obj):
    temp = {key: value for key, value in obj.__dict__.items() if isinstance(value, int)}
    return obj.__class__(**temp)


def main():
    object1 = Some(a=1, b="qqqq", c=4.1, d='w', e=9, f=54)
    object2 = create_object(object1)
    print(object2.a)
    print(object2.e)
    print(object2.f)
    print(object2.d)


if __name__ == '__main__':
    main()
