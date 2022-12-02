def html(func):
    def wrapper(*args):
        def inner(*args):
            val = func(*args)
            return "<html>{}</html>".format(val)
        return inner(*args)
    return wrapper


@html
def get_tag(text):
    return text


if __name__ == '__main__':
    print(get_tag("Hello"))
