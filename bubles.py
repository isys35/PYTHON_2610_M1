from random import randint

a = []
for i in range(20):
    a.append(randint(0, 1000))
print(a)
z = len(a)
print(z)
l = 0
while l != (z - 1):
    j = 0
    l = 0
    while j < z - 1:
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            j = j + 1
            print(a)
        else:
            j = j + 1
            l = l + 1
            print(a)

print("конец")