def days_of_the_week(a):
    return {
       a == 1: "Monday",
       a == 2: "Tuesday",
       a == 3: "Wednesday",
       a == 4: "Thursday",
       a == 5: "Friday",
       a == 6: "Saturday",
       a == 7: "Sunday"
    }[True]


day = int(input("Enter the number: "))
print(days_of_the_week(day))
