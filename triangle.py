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
                sum_ab = a + b
                sum_ac = a + c
                sum_bc = b + c
                ch_a = (a < sum_ab) and (a < sum_ac) and (a < sum_bc)
                ch_b = (b < sum_ab) and (b < sum_ac) and (b < sum_bc)
                ch_c = (c < sum_ab) and (c < sum_ac) and (c < sum_bc)
                if ch_a == True and ch_b == True and ch_c == True:
                        print("Треугольник существует")
                else:
                        print("Треугольник не существует")



else:
        print("Нужно было ввести три числа")