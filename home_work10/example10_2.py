'''Написать функцию-генератор для выделения слов из  текста
(слова разделяются пробелом, либо переносом строки ‘\n’).
Список всех слов при этом в функции не создавать.'''

import re


def generation_words(line):
    word = ''
    for letter in line:
        if re.match(r'\w', letter):
            word += letter
        elif len(word) > 0:
            yield word
            word = ''
    yield word


if __name__ == '__main__':
    for item in generation_words('Здесь должен быть любой текст для проверки, поэтому именно этот здесь и есть'):
        print(item)
