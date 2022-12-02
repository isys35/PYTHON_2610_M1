def get(func):
    def wrapper():
        result = func()
        return "<html>" + result + "<html>"
    return wrapper

@get
def say_hi():
    return "привет"

a = say_hi()
print(a)