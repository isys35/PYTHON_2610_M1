from statistics import mean


def mean_min_mas(*num):
    return [min(num), max(num), mean(num)]


new_list = mean_min_mas(1, 2, 4, 0, -5, 5, 8, 9, 7, 6)
print(new_list)
