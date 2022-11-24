from statistics import mean


def statistical_analysis(*args):
    return [mean(*args), min(*args), max(*args)]


numbers = (1, 2, -6, 10)
print(statistical_analysis(numbers))
