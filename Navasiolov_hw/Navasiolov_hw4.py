print("Зравствуйте, введите ваше имя! ")
name = input("Имя: ")
print("\nЗдрвавствуйте ", name)
order = int(input("\nВведите сумму заказа:"))
tea = order * 0.18
tax = order * 0.04
amount = order + tea + tax
print("\nСумма заказа: ", order)
print("Чайвые: ", tea)
print("Налог: ", tax)
print("\nСумма к оплате: ", amount)
print("Хорошего дня! ", name)
input("загрузка вируса.....")