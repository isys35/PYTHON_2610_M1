def triangle():
    '''Функция производит расчет возможности содания треугольника
    ничего не принимает и ничего не возвращает'''
    if first_meaning + second_meaning > third_meaning and \
            first_meaning + third_meaning > second_meaning and \
            second_meaning + third_meaning > first_meaning:
        print("Да, такой треугольник возможен")
    else:
        print("Нет, построение такого треугольника невозможно")


if __name__ == '__main__':
    first_meaning = float(input('первое значение = '))
    second_meaning = float(input('второе значение = '))
    third_meaning = float(input('третье значение = '))
    triangle()
