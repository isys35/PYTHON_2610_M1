authors_books = {
        "Уилсон": "Спин",
        "Зусак": "Книжный вор",
        "Вейер": "Марсианин",
        "Каку": "Физика невозможного",
        "Брэдбери": "451 по Фаренгейту"
}

flg = 0
for author, book in authors_books.items():
    answer = input(f"Автор книги \"{book}\": ")
    if answer.capitalize() == author:
        flg += 1
print(f"Кол-во правильных ответов: {flg}/5")
print("\nПРАВИЛЬНЫЕ ОТВЕТЫ:")
for author, book in authors_books.items():
    print(f"\"{book}\" -- {author}")
