def odd_num(arr, k):
    new = []
    for i in range(k):
        if arr[i] % 2 != 0:
            new.append(arr[i])
    return new


list_1 = []
print("Enter a sequence of numbers(!letter)")
while True:
    try:
        tmp = int(input())
        list_1.append(tmp)
    except ValueError:
        print("Enter a letter; recording a list completed")
        break

print(list_1)
new_list = odd_num(list_1, len(list_1))
print("The first list", list_1)
print("Odd numbers in list:", new_list)
