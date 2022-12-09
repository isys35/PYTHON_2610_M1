#  Напишите программу с функцией, аргументом которой передается числовой список, а результатом является еще один список,
#  в который включены только нечетные числа из списка-аргумента.
from random import randint

num_list = [randint(0, 100) for i in range(10)]


def odd_num(test_list):
    result_list = []
    for i in test_list:
        if i % 2 != 0:
            result_list.append(i)
    return result_list


if __name__ == '__main__':
    print(num_list)
    print(odd_num(num_list))
