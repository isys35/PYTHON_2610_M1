list_1 = [1, 2]
list_2 = [1, 2, list_1]

list_3 = list_2.copy()
print(list_1, id(list_1))
print(list_2, id(list_2))
print(list_3, id(list_3))

print(id(list_2[2]))
print(id(list_3[2]))

list_3[1][2] = 0

print(list_1)