import re


def generation_words(line):
    word = ""
    for letter in line:
        if re.match(r'\w', letter):
            word += letter
        elif len(word) > 0:
            yield word
            word = ""
    yield word


for item in generation_words("Генераторные функции - записываются как нормальные операторы def,"
                             "но в них применяются операторы yield, чтобы возвращать по одному результату"
                             "за раз, приостанавливать выполнение с сохранением состояния и возобновлять его"
                             "между выдачами."):
    print(item)
