def odd_num(arr):
    return [i for i in arr if i % 2 != 0]


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
new_list = odd_num(list_1)
print("The first list", list_1)
print("Odd numbers in list:", new_list)
