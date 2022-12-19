def multiplication(number):
    '''Функция получает одно значение, которое вводит пользователь,
        умножает его от 1 до 10 и выводит все значения.
        но ничего не возвращает.'''
    if number <= 12:
        for i in range(1, 11):
            print(i * number, end="\t")
    else:
        print("Вы ввели число не в диапазоне от 1 до 12.")


if __name__ == '__main__':
    user_number = int(input("Введите целое число от 1 до 12:\n "))
    multiplication(user_number)