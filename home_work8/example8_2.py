
from random import randint
from typing import List


def generate_list(size: int) -> List[int]:
    list = []
    for i in range(size):
        list.append(randint(1, 100))
    return list


def odd_num(unsorted: list) -> List[int]:
    return [i for i in unsorted if i % 2 != 0]


if __name__ == '__main__':
    list = generate_list(10)
    t = odd_num(list)
    print(list)
    print(t)