# 3. Декоратор для создания тегов
# Напишите функцию-декоратор, чтобы она заключала возвращаемое значение упакованной функции в теги "<html>" и "</html>"
# Обернутая функция должна возвращать подобный результат:
# <html>hello<html>

def decorator_for_tags(func):
    def wrapper(arg):
        in_tags = f"<html>{func(arg)}<html>"
        return in_tags

    return wrapper


@decorator_for_tags
def hello(message):
    return message


if __name__ == '__main__':
    print(hello("hello"))
