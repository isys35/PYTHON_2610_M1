def html(func):
    def wrapper(*args):
        def inner(*args):
            val = func(*args)
            return "<html>{}</html>".format(val)
        return inner(*args)
    return wrapper


@html
def plus_html(text):
    return text


if __name__ == '__main__':
    print(plus_html("Hello"))
