def diet_printer(function):
    def wrapper(*args):
        print(f"Client consumed {function(*args)} calories per day.")

    return wrapper


def html_template(function):
    def wrapper(*args, **kwargs):
        print(f"<html>{function(*args, **kwargs)}</html>")

    return wrapper
