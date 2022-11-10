a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))
if a+b>c and a+c>b and b+c>a:
    print("Треугольник существует")
else:
    print("Треугольник не существует")