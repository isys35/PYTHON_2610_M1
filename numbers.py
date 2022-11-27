x = input("Введите три числа через пробел:").split(" ")
y = len(x)
if y == 3:
        first_str = x[0].isdigit()
        second_str = x[1].isdigit()
        third_str = x[2].isdigit()
        if first_str == True and second_str == True and third_str == True:
                a = int(x[0])
                b = int(x[1])
                c = int(x[2])
                d = [a, b, c]
                d.sort()
                a = int(d[0])
                b = int(d[1])
                c = int(d[2])
                if (c-b) == (b-a):
                        print("Последовательность существет")

                else:
                        print("Последовательности нет")
else:
        print("Нужно было ввести три числа")