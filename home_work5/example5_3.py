def week(number):
    '''Функция week принимает одно значение (целое число)
    и сравнивает его с днями неделями и ничего не возвращает'''
    match number:
        case 1: print("Понедельник")
        case 2: print("Вторник")
        case 3: print("Среда")
        case 4: print("Четверг")
        case 5: print("Пятница")
        case 6: print("Суббота")
        case 7: print("Воскресенье")
        case _: print("Вы ввели число которое не в диапазоне от 1 до 7 (включительно)")


if __name__ == '__main__':
    number_user = int(input('Введите целое число от 1 до 7 (включительно) = '))
    week(number_user)