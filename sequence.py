# Задача 2. Напишите программу, в которой пользователь вводит три целых числа,
# а программа проверяет, являются ли эти числа тремя последовательными
# элементами арифметической последовательности. В арифметической последовательности
# каждый новый член получается прибавлением к предыдущему определенного фиксированного числа.
a = int(input("Введите первое число: "))
d = int(input("Введите постоянное число: "))
n = int(input("Введите n-член: "))
b = a+d*(n-1)
print (b)
