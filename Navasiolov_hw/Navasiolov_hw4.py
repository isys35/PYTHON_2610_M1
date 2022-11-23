print("Зравствуйте, введите ваше имя! ")
name = input("Имя: ")
print("\nЗдрвавствуйте ", name)
Order = int(input("\nВведите сумму заказа:" ))
Tea = Order * 0.18
Tax = Order * 0.04
Amount = Order + Tea + Tax
print("\nСумма заказа: ", Order)
print("Чайвые: ", Tea)
print("Налог: ", Tax)
print("\nСумма к оплате: ", Amount)
print("Хорошего дня! ", name)