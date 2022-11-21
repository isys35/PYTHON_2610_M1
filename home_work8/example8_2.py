
from random import randint
from typing import List


def generate_list(size: int) -> List[int]:
    list = []
    for i in range(size):
        list.append(randint(1, 100))
    return list


def odd_num(unsorted: list) -> List[int]:
    sorted_list = []
    for i in unsorted:
        if i % 2 != 0:
            sorted_list.append(i)
    return sorted_list


if __name__ == '__main__':
    list = generate_list(10)
    t = odd_num(list)
    print(list)
    print(t)