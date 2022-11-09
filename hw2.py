sum = int(input("Введите сумму: "))  #Счёт
tips = 0.18 * sum                    #Сумма чаевых без учёта налога
tax = 0.04 * (sum - tips)            #Сумма налога
total = sum - tips - tax             #Сумма для оплаты с учётом вычета чаевых и налога
print("Сумма равна: ", sum, "р, к ")
print("Количество чаевых : ", tips, "р, к ")
print("Сумма налога: ",tax, "р, к ")
print("Итого к оплате: ",total, "р, к ")


a = int(input("Введите значение числа (a): "))
b = int(input("Введите значение числа (b): "))
sum = a + b
substraction = a - b
multiplication = a * b
division = a / b
division1 = a // b
degree = a ** b
print("Сумма a и b  : ", sum )
print("Разница между a и b : ", substraction )
print("Произведение a и b: ", multiplication )
print("Частное от деления a на b: ", division )
print("Остаток от деления a на b: ", division1 )
print("Результат возведения числа a в степень b: ", degree )