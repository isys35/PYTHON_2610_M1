#  вопрос по этому скрипту будит на собеседовании"
def add_six(list_to_add):
    list_to_add.append(6)


init_list = [1, 2, 3]
add_six(init_list)

print(init_list)


def add_six(list_to_add):
    list_to_add.append(6)

def send_message(name, message):
    print(f"{name}, {message}!")

# на сабезе ( arg является картэжам)
def greet(*args):
    for arg in args:
        print(arg)

def greet_2(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}", {value})


if __name__ == "__main__":
    init_list = [1, 2, 3]
    add_six(init_list)
    print(init_list)
    send_message("Анатолий", "Здравствуйте")
    send_message(name="Анатолий")
    send_message(message= "Я тут")
    greet("Привет", "как дела", "нормально")
    example_dict = {"name": "An",}