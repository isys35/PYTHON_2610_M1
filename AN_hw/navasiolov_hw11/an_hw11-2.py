"""
Задача 3.

Напишите программу, в которой пользователь
вводит целое число от 1 до 7 включительно,
а программа выводит название дня недели,
соответствующее этому числу
("Понедельник" для 1, "Вторник " для 2, и так далее).
"""
def is_calendar(command: int):
    """
       Функция проверяет является ли введенные числа днями недели
    :param command: "1", "2", "3", "4", "5", "6", "7"
    :return: bool
    """

def main() -> is_calendar:
    """ Точка входа"""
command: int = int(input("Введите число дня недели от 1 до 7 :"))
match command:
    case 1:
        print("Понидельник")
    case 2:
        print("фторник")
    case 3:
        print("Среда")
    case 4:
        print("Четверг")
    case 5:
        print("Пятница")
    case 6:
        print("Суббота")
    case 7:
        print("Воскресенье")
print("\n  Хорошего дня !")


if __name__ == "__main__":
    main()

     # Предыдущий вариант
#command: = input("Введите число дня недели от 1 до 7 :")
#match command:
    #case "1":
        #print("Понидельник")
    #case "2":
        #print("фторник")
    #case "3":
        #print("Среда")
    #case "4":
#        print("Четверг")
#    case "5":
#        print("Пятница")
#    case "6":
#        print("Суббота")
#    case "7":
#        print("Воскресенье")
#print("\n  Хорошего дня !")