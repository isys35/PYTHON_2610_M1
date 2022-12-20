'''Напишите программу с функцией, аргументом которой передается
числовой список, а результатом является еще один список, в который
включены только нечетные числа из списка-аргумента.'''
from random import randint
from typing import List

'''Создается фукция где пользователь вводит размер списка, а список наполняется randomom.'''


def generate_list(size: int) -> List[int]:
    lst = []
    for i in range(size):
        lst.append(randint(-100, 100))
    return lst


'''Создается функция которая уже сортирует созданный список на нечетные числа'''


def odd_num(unsorted: list) -> List[int]:
    return [i for i in unsorted if i % 2 != 0]


if __name__ == '__main__':
    numbers = int(input('Количесво значений в списке:\n'))
    user_lst = generate_list(numbers)
    unsorted_lst = odd_num(user_lst)
    print(user_lst)
    print(unsorted_lst)
