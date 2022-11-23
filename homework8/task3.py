from statistics import mean


def mean_min_max(*num):
    return [min(num), max(num), mean(num)]


list_result = mean_min_max(2, 9, 0, 5, -5, 1, 7, -8)
print(list_result)
