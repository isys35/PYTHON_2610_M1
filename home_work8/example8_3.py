from functools import reduce
import operator


def mean():
    lst = [1.78, 2, 5, 6.53, 10, -8.13, -15, 25.79, 4, 233.98]
    lst_len = len(lst)
    list = reduce(operator.add, lst) / lst_len
    max(lst)
    min(lst)
    print("Среднее значение:\n", round(list, 2))
    print("Минимальное значение:\n", min(lst))
    print("Максимальное значение:\n", max(lst))


mean()