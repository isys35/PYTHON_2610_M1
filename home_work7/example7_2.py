'''Предложите пользователю ввести число от 1 до 12.
Выведите таблицу умножения для этого числа'''


def multiplication(numbers: int) -> None:
    '''Функция получает одно значение, которое вводит пользователь,
    умножает его от 1 до 10 и выводит все значения.
    но ничего не возвращает.'''
    number = 1
    if numbers <= 12:
        while number <= 10:
            print(numbers * number, end="\t")
            number += 1
    else:
        print("Вы ввели число не в диапазоне от 1 до 12.")


def main() -> None:
    user_number = int(input("Введите целое число от 1 до 12:\n"))
    multiplication(user_number)


if __name__ == '__main__':
    main()
