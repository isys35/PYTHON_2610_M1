try:
    sum =float(input('сумма заказа = '))
    tips = sum * 0.18
    tax = sum * 0.04
    total = sum + tips + tax
    print('сумма налога = ', round(tax, 2))
    print(f'сумма чаевых официанту = {tips:.2f}')
    print('итог = {:.2f}'.format(total))
except ValueError as a:
    print('Сведения об исключении:', a)
    print('Вы ввели буквы, а не числа.\nБудьте внимательней.')