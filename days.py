#Задача 3.Напишите программу, в которой пользователь вводит целое число от 1 до 7 включительно,
# а программа выводит название дня недели, соответствующее этому числу
# ("Понедельник" для 1, "Вторник " для 2, и так далее).

a = int(input('Введите число от 1 до 7: '))
res = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
print(res[a-1])