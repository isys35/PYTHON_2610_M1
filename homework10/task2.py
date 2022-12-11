def generate_words(a):
    word = ""
    for i in a:
        if i == " " or i == "\n":
            yield word
            word = ""
        else:
            word += i
    yield word


if __name__ == '__main__':
    string = f"Time has many faces. Time measures life, months and years. \n" \
             "Time erases mountains and creates stars. \nAnd how many things " \
             "happen between two heartbeats! \nIt is difficult to live on such " \
             "different scales of time, they tear you apart."
    for elem in generate_words(string):
        print(elem)
