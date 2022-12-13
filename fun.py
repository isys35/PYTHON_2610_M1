def filter_odd_numbers(init_list):
    result_list = []
    for number in init_list:
        if number % 2 == 0:
            result_list.append(number)
    result_list.sort()
    return result_list

init_list = [1, 23, 42, 2, 12]
print(init_list)
print(filter_odd_numbers(init_list))