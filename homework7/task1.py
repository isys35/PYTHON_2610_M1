from random import randint

amount_elements = 10
ready_list = []
for i in range(amount_elements):
    ready_list.append(randint(1, 99))
print(ready_list)

for i in range(amount_elements - 1):
    for j in range(amount_elements - i - 1):
        if ready_list[j] > ready_list[j + 1]:
            ready_list[j], ready_list[j + 1] = ready_list[j + 1], ready_list[j]

print(ready_list)

