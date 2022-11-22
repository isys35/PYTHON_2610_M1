from statistics import mean


def max_min_mean(*number):
    return [max(number), min(number), round(mean(number), 2)]


new_list = max_min_mean(1.78, 2, 5, 6.53, 10, -8.13, -15, 25.79, 4, 233.98)
print(new_list)