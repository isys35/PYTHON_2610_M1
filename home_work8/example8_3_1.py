'''Напишите программу, в которой описывается функция с произвольным количеством числовых аргументов,
а результатом возвращается список из трех элементов:
среднее значение среди аргументов,
максимальное значение среди аргументов и минимальное значение среди аргументов.'''
from statistics import mean
from random import randint

'''Создаетс функция в которую передается список из чисел, а внутренняя функция mean вычесляет среднее значение.
При этом сам список из произвольных чисел заполняется random, пользователь вводит только количество значений в списке.'''


def max_min_mean(*number: int) -> list[float]:
    return [max(number), min(number), round(mean(number), 2)]


def main() -> None:
    lst = []
    elements = int(input('Количесво значений в списке:\n'))
    for i in range(elements):
        lst.append(randint(-100, 100))
    print(lst)
    new_lst = max_min_mean(*lst)
    print(new_lst)


if __name__ == '__main__':
    main()
