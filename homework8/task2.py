try:
    order_price = float(input("Введите сумму заказа: "))
    if order_price <= 0:
        raise ValueError("Сумма заказа некорректна")
    tips = order_price * 0.18
    tax = order_price * 0.04
    total = order_price + tax + tips

    print("\nСумма заказа: ", order_price)
    print("Налог составил: %.2f" % tax)
    print("Чаевые:  %.2f" % tips)
    print("\nИтоговая сумма составила: %.2f" % total)
except ValueError as error_message:
    print(f"Некорректные данные для обработки: {error_message}")
except Exception as err:
    print(f"Что-то пошло не так: {err}")
