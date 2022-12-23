def calculator(a: int, b: int) -> None:
    '''Функция производит расчет калькулятора
    принимает два с плавающей точкой значения a и b'''
    c = a + b
    print('сумма значений = ', c)
    c = a - b
    print('разница значений = ', c)
    c = a * b
    print('произведение чисел = ', c)
    c = a // b
    print('целочисленное деление = ', c)
    c = a % b
    print('остаток от деления = ', c)
    c = a ** b
    print('результат возведения первого числа в степень второго = ', c)


def main() -> None:
    first = float(input('первое значение = '))
    second = float(input('второе значение = '))
    calculator(first, second)


if __name__ == '__main__':
    main()
