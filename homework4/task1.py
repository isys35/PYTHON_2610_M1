order_price = float(input("Введите сумму заказа: "))
tips = order_price * 0.18
tax = order_price * 0.04
total = order_price + tax + tips

print("\nСумма заказа: ", order_price)
print("Налог составил: %.2f" % tax)
print("Чаевые:  %.2f" % tips)
print("\nИтоговая сумма составила: %.2f" % total)
