def arithmetic_subsequence(first_number, second_number, third_number):
    '''Функция производит расчет являются ли 3 числа арифметической последовательностью
    принимает 3 значения и ничего не возвращает'''
    if second_number - first_number == third_number - second_number:
        print("Это арифметическая последовательность")
    else:
        print("Не явлеяется арифметической последовательностью")


if __name__ == '__main__':
    number_1 = int(input('Введите целое первое значение = '))
    number_2 = int(input('Введите целое второе значение = '))
    number_3 = int(input('Введите целое третье значение = '))
    arithmetic_subsequence(number_1, number_2, number_3)
