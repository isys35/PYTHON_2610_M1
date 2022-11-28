# Задача 3
# Спросите у пользователя, скольких людей он хочет пригласить на вечеринку. Если будет введено число меньше 10,
# запросите имена и после каждого имени выведите строку «[имя] has been invited». Если введенное число больше или
# равно 10, выведите сообщение «Too many people».

# от себя добавил словарь со списком гостей и его вывод через принт

amount_guest = int(input("Сколько гостей планируется на вечеринке? "))
list_guest = [i + 1 for i in range(0, amount_guest)]
dict_guest = dict.fromkeys(list_guest)
if amount_guest < 10:
    number_guest = 1
    for guest in list_guest:
        name_guest = input(f"Введите имя гостя №{number_guest}: ")
        print(f"{name_guest} has been invited")
        dict_guest[number_guest] = name_guest
        number_guest += 1
    print("Список гостей:")
    for key, value in dict_guest.items():
        print(f"Гость {key}: {value}")
elif amount_guest > 10:
    print("Too many people!")
