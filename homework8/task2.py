from random import randint


def list_generation(amount_elements):
    list1 = []
    for i in range(amount_elements):
        list1.append(randint(1, 100))
    return list1


def odd_list(unsorted):
    return [i for i in unsorted if i % 2 != 0]


if __name__ == '__main__':
    list1 = list_generation(10)
    sort_list = odd_list(list1)
    print(list1)
    print(sort_list)
