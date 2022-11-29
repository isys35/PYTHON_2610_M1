import re


def words_generator(string):
    word = ""
    for letter in string:
        if re.match(r'\w', letter):
            word += letter
        elif len(word) > 0:
            yield word
            word = ""
    yield word


for item in words_generator("Lorem ipsum, dolor sit\namet!!!"):
    print(item)
