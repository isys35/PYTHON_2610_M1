def decorators(function):
    def wrapper(*args):
        wrap = function(*args)
        return "<html>{}</html>".format(wrap)
    return wrapper


@decorators
def tag(html):
    return html


if __name__ == '__main__':
    try:
        finish = tag("hello")
        print(finish)
    except Exception:
        print("Что-то пошло не так.\nПопробуйте снова.")