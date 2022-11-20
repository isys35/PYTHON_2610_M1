from random import randint

elements = 7
list = []
for i in range(elements):
    list.append(randint(1, 101))
print(list)

for i in range(elements - 1):
    for j in range(elements - i - 1):
        if list[j] > list[j + 1]:
            list[j], list[j + 1] = list[j + 1], list[j]

print(list)