sum = int(input('сумма заказа = '))
tips = sum * 0.18
tax = sum * 0.04
total = sum - tips - tax
print('сумма налога = ', tax)
print('сумма чаевых официанту = ', tips)
print('итог = ', round(total, 2))