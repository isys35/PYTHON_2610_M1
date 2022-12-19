def party(number, name):
    '''Функция принимает два значения number и name. Количество людей и их имена.
    Если людей больше 10, то скажет, что много людей.
    После того как пользователь вводит количесво людей, потом он вводит имена людей, чтобы те получили приглашения.'''
    if number < 10:
        user_list = name.split(", ")
        for i in user_list:
            print(f"{i.title()}, has been invited.")
    else:
        print("Too many people.")


if __name__ == '__main__':
    user_number = int(input("Сколько людей вы хотите пригласить на вечеринку:\n"))
    user_str = input("Введите имена людей, через запятую, которых хотите пригласить:\n")
    party(user_number, user_str)