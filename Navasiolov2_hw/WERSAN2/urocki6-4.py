week = {
    1: "Понидельник",
    2: "Фторник",
    3: "Среда",
    4: "Четверг",
    5: "Пятница",
    6: "Суббота",
    7: "Воскресенье",
}

number = int(input("Введите число: "))
#print(week[number])
week_name = week.get(number)
if week_name:
    print(week_name)
else:
    print("erorre!!!")