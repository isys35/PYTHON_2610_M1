def restaurant(summa: float) -> None:
    '''Функция производит расчет налога, чаевых официанту и итоговый расчет
    принимает одно с плавающей точкой значение summa'''
    tips = summa * 0.18
    tax = summa * 0.04
    total = summa + tips + tax
    print(f'сумма налога = {tax:.2f}')
    print(f'сумма чаевых официанту = {tips:.2f}')
    print('итог = ', round(total, 2))


def main() -> None:
    summa_user = float(input('сумма заказа = '))
    restaurant(summa_user)


if __name__ == '__main__':
    main()
