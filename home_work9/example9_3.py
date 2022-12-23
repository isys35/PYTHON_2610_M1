'''Напишите функцию-декоратор,
чтобы она  заключала возвращаемое значение упакованной функции в теги
"<html>" и "</html>" '''

'''Создается функция декоратор.'''


def decorators(function):
    def wrapper(*args):
        wrap = function(*args)
        return "<html>{}</html>".format(wrap)

    return wrapper


'''Теперь эта функция декортатор накладывается на фунекцию tag.'''


@decorators
def tag(html):
    return html


def main() -> None:
    try:
        finish = tag("hello")
        print(finish)
    except Exception:
        print("Что-то пошло не так.\nПопробуйте снова.")


if __name__ == '__main__':
    main()
