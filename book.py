my_lib = {
    "Толстой" : "Война и мир",
    "Твен" : "Приключения Гекльберри Финна",
    "Элиот" : "Мидлмарч",
    "Доил" : "Шерлок Холмс",
    "Стивенсон" : "Остров сокровищ",
    "Ремарк" : "На западно фронте без перемен"
}
my_mean = my_lib.values()
x = 0
for book in my_mean:
    z = input(f"Кто написал {book} ? :")
    if (z, book) in my_lib.items():
       print("Верно")
       x = x + 1
    else:
        print("Не верно")
print(f"Вы набрали {x} из 6 очков")