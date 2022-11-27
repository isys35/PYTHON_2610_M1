x = int(input("Введите число от 1 до 7:"))
if x == 1 or 2 or 3 or 4 or 5 or 6 or 7:
    if x == 1:
        print("Понедельник")
    else:
        if x == 2:
            print("Вторник")
        else:
            if x == 3:
                print("Среда")
            else:
                if x == 4:
                    print("Четверг")
                else:
                    if x == 5:
                        print("ПЯТНИЦА")
                    else:
                        if x == 6:
                            print("Суббота")
                        else:
                             print("Воскресенье")
else:
    print("Нужно было ввести число от 1 - 7")
