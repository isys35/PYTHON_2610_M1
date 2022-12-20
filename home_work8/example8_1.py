'''ValueError - провертка не вел ли пользователь букву вместо цифры, а если ввел, то выскачет предупреждение'''
try:
    first_number = int(input('Введите целое первое значение = '))
    second_number = int(input('Введите целое второе значение = '))
    third_number = int(input('Введите целое третье значение = '))
    if second_number - first_number == third_number - second_number:
        print("Это арифметическая последовательность")
    else:
        print("Не явлеяется арифметической последовательностью")
except ValueError:
    print("Вы ввели буквы, а не числа.\nБудьте внимательней.")