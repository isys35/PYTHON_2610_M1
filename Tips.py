check_amount = int(input("Введите сумму чека :"))
check_amount = int(check_amount)
tax = check_amount * 0.04
tips = (check_amount - tax) * 0.18
print("Сумма чека :", check_amount, "руб.", "\nСумма налога 4% :", "%.2f"%tax, "руб.", "\nСумма чаевых :", "%.2f"%tips, "руб.")
