try:
    user_number1 = float(input('первое значение = '))
    user_number2 = float(input('второе значение = '))
    if user_number2 == 0:
        raise ZeroDivisionError
    c = user_number1 + user_number2
    print(f'сумма значений =  {c:.2f}')
    c = user_number1 - user_number2
    print(f'разница значений = {c:.2f}')
    c = user_number1 * user_number2
    print(f'произведение чисел = {c:.2f}')
    c = user_number1 // user_number2
    print(f'целочисленное деление = {c:.2f}')
    c = user_number1 % user_number2
    print(f'остаток от деления = {c:.2f}')
    c = user_number1 ** user_number2
    print(f'результат возведения первого числа в степень второго = {c:.2f}')
except ValueError:
    print('Вы ввели буквы, а не числа.\nБудьте внимательней.\nПопробуйте снова.')
except ZeroDivisionError:
    print('На ноль (0) делить нельзя.\nПопробуйте снова.')
except BaseException:
    print("Общее исключение.\nПопробуйте снова.")
