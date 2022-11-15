my_list = ['a', 'b', 'c', 'd', 'e', 'f']
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

print(my_list)
print(my_dict)

print(len(my_list))
print(len(my_dict))

print('a' in my_list)

# проверяет в ключах
print('a' in my_list)
print('a' in my_dict.keys())

# проверяет в значениях словоря

print(4 in my_dict.values())

# проверяем наличия пар
print(('c', 3) in my_dict.items())

for item in my_dict:
    print(item)

for key, pet in my_dict.items():
    print(key, pet)

# min() max() sum()

# Кол-во 'a'
my_dict.count('a')

print(my_dict.index('d'))
