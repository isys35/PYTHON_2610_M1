print("Какова сумма вашего заказа?")
a = float(input())
tax = float(round(a * 0.18, 2))
tips = float(round(a * 0.04, 2))
total = float(round(a + tax + tips, 2))
print("Сумма чаевых: ", tax)
print("Налог: ", tips)
print("Итого сумма заказа составила: ", total)

