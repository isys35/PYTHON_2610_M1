def books():
    '''Функция books ничего не принимает, а только сравнивает ответы пользователя,
    выводит резильтат, но ничего не возвращает.
    Все остается в самой функции, она ничего не возвращает'''
    dic_book_authors = {
        "Кен кизи": "Пролетая над гнездом кукушки",
        "Морис Леблан": "Приключения Арсена Люпена",
        "Артур Конан Дойл": "Шерлок Холмс",
        "Артур Хэйли": "Аэропорт",
        "Оскар Уайльд": "Портрет Дориана Грея"
    }
    result = 0
    for key, value in dic_book_authors.items():
        user_answer = input(f"Введите Имя и Фамилию автора произведения: {value}\n")
        if user_answer.title() == key.title():
            result += 1
            print("Правильно")
        else:
            print("Не правильно")
    print(f"Ваш результат: ", result)


if __name__ == '__main__':
    books()


'''Либо через match/case
result = 0
for key, value in dic_book_authors.items():
    user_answer = input(f"Введите Имя и Фамилию автора произведения: {value}\n")
    match user_answer:
        case "кен кизи":
            result += 1
            print("Правильно")
        case "морис леблан":
            result += 1
            print("Правильно")
        case "артур конан дойл":
            result += 1
            print("Правильно")
        case "артур хэйли":
            result += 1
            print("Правильно")
        case "оскар уайльд":
            result += 1
            print("Правильно")
        case _:
            print("Не верно")
print(f"Ваш результат: ", result)'''