user_number = int(input("Сколько людей вы хотите пригласить на вечеринку:\n "))
if user_number < 10:
    user_str = input("Введите имена людей, через запятую, которых хотите пригласить:\n")
    user_list = user_str.split(", ")
    for i in user_list:
        print(f"{i} has been invited")
else:
    print("Too many people")