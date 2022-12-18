tips = 0.18
tax = 0.04
summa = input("Введите сумму заказа:")
summa = float(summa)
tips = summa * tips
tax = summa * tax
total = summa + tips + tax
print("Налог:", "%.2f" % round(tax, 2))
print("Чаевые:", "%.2f" % round(tips, 2))
print("К оплате:", "%.2f" % round(total, 2))