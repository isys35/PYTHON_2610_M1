# Напишите программу, в которой пользователь вводит три числа, а программа определяет, может ли существовать
# треугольник со сторонами, длина которых равняется введенным значениям. Условие существования треугольника такое:
# сумма двух любых (из трех введенных) чисел должна быть больше третьего числа.
a = input("Введите первое число: ")
b = input("Введите второе число: ")
c = input("Введите третье число: ")
if a+b > c and a+c > b:
    print("Ура, треугольник с такими сторонами может существовать")
else:
    print("Увы, существование треугольника с такими сторонами невозможно")

