def sort_bubble(arr, k):
    for i in range(k):
        for j in range(k-i-1):
            if arr[j+1] < arr[j]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


x = []
print("Enter a sequence of numbers(!666)")
while True:
    tmp = int(input())
    if tmp != 666:
        x.append(tmp)
    else:
        break
print("Initial list:", x)
sort_bubble(x, len(x))
print("Sorted list:", x)
