print("Enter 3 numbers")
num1 = int(input())
num2 = int(input())
num3 = int(input())
if num1+num2 > num3 and num1+num3 > num2 and num2+num3 > num1:
    print("Triangle with such sides exist")
else:
    print("Triangle with such sides doesn't exist")
