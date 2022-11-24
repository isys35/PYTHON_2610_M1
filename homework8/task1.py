try:
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    print("Сумма чисел a и b равна: ", a + b)
    print("Разность чисел a и b равна: ", a - b)
    print("Произведение чисел a и b равно: ", a * b)
    print("Частное от деления чиселел a и b равно: ", a / b)
    print("Остаток от деления числа a на число b равен: ", a % b)
    print("Число a  в степени b равно: ", a ** b)
except ZeroDivisionError:
    print("ОШИБКА!!! Попытка деления на ноль")
except ValueError:
    print("ОШИБКА!!! Неверный ввод данных")
except Exception as err:
    print(f"Что-то пошло не так: {err}")
