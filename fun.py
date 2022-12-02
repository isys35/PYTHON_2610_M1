def filter_odd_numbers(init_list):
    result_list = []
    for number in init_list:
        if number % 2 == 0:
            result_list.append(number)
    result_list.sort()
    return result_list

