# 5 Генератор для получения слов
# Написать функцию-генератор для выделения слов из текста (слова разделяются пробелом, либо переносом строки ‘\n’).
# Список всех слов при этом в функции не создавать.
from re import split

text = "Отладка кода вдвое сложнее, чем его написание. Так что если вы пишете код настолько умно, " \
       "насколько можете, то вы по определению недостаточно сообразительны, чтобы его отлаживать."


def gen(text_inner):
    text_iter = iter(text_inner)
    word = ""
    for item in text_iter:
        if item.isalpha():
            word = word + item
        elif item == ' ':
            yield word
            word = ""
        else:
            continue


if __name__ == '__main__':
    gen = gen(text)
    print(gen)
    for item in gen:
        print(item)
