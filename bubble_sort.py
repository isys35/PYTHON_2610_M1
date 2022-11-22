import numpy


def bubble_sort(numbers_list):
    for i in range(len(numbers_list) - 1, 0, -1):
        for j in range(i):
            if numbers_list[j] > numbers_list[j + 1]:
                numbers_list[j], numbers_list[j + 1] = numbers_list[j + 1], numbers_list[j]
    return numbers_list


size = int(input("Enter list size: "))
print(bubble_sort(numpy.random.randint(0, 100, size)))
