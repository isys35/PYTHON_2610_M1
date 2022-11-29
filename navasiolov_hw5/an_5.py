print("\n!Создайте Треугольник!")
side_1 = int(input("\n--> Сторона А: "))
side_2 = int(input("--> Сторона Б: "))
side_3 = int(input("--> Сторона Ц: "))
if side_1 + side_2 > side_3:
    print(" Треугольник ")
else:
    print(" Пока не ")
if side_2 + side_3 > side_1:
    print(" Этот")
else:
    print(" Не ")
if side_3 + side_1 > side_2:
    print(" Существует")
else:
    print(" Не доработан! ")
