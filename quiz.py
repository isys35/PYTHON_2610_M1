import sys

quiz = {
    'Пушкин': 'Золотой петушок',
    'Толстой': 'Война и мир',
    'Гоголь': 'Вий'
}
hello = input("Привет! Хочешь пройти викторину? Yes/No\n")
if hello.lower() != "yes":
   sys.exit()
right_answers_count = 0
for author, title in quiz.items():
    answer = input(f"Назовите автора произведения {title}: ")
    if answer.lower() == author.lower():
        right_answers_count += 1
        print("Верно!")
    else:
        print("Вы ошиблись.")
print(f"Ваш результат: {right_answers_count} из {len(quiz)}")
