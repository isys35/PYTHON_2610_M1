# Задача 2
# Предложите пользователю ввести число от 1 до 12. Выведите таблицу умножения для этого числа.

user_number = int(input("Введите число от 1 до 12: "))
list_number = [i + 1 for i in range(0, 9)]
for number in list_number:
    result = number * user_number
    print(f"{number} x {user_number} = {result}")
