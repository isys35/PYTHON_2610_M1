'''Напишите программу, в которой пользователь вводит три целых числа,
а программа проверяет, являются ли эти числа тремя последовательными элементами арифметической последовательности.
В арифметической последовательности каждый новый член получается прибавлением к
предыдущему определенного фиксированного числа.'''




def arithmetic_subsequence(first_number: int, second_number: int, third_number: int) -> bool:
    '''Функция производит расчет являются ли 3 числа арифметической последовательностью
    принимает 3 значения и возвращает True или False
    param: first_number - первое значение
    param: second_number - второе значение
    param: third_number - третье значение
    return bool'''
    if second_number - first_number == third_number - second_number:
        return True
    return False


def main() -> None:
    '''Точка входа'''
    number_1 = int(input('Введите целое первое значение = '))
    number_2 = int(input('Введите целое второе значение = '))
    number_3 = int(input('Введите целое третье значение = '))
    if arithmetic_subsequence(number_1, number_2, number_3):
        print("Это арифметическая последовательность")
    else:
        print("Не явлеяется арифметической последовательностью")


if __name__ == '__main__':
    main()
