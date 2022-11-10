first_number = int(input('Введите целое первое значение = '))
second_number = int(input('Введите целое второе значение = '))
third_number = int(input('Введите целое третье значение = '))
if second_number - first_number == third_number - second_number:
    print("Это арифметическая последовательность")
else:
    print("Не явлеяется арифметической последовательностью")