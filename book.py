my_lib = {
    "Толстой" : "Война и мир",
    "Твен" : "Приключения Гекльберри Финна",
    "Элиот" : "Мидлмарч",
    "Доил" : "Шерлок Холмс",
    "Стивенсон" : "Остров сокровищ",
    "Ремарк" : "На западно фронте без перемен"
}
point = 0
for author, book in my_lib.items():
    answer_author = input(f"Кто написал {book} ? :") 
    if answer_author == author:
       print("Верно")
       point = point + 1
    else:
        print("Не верно")
print(f"Вы набрали {point} из 6 очков")
