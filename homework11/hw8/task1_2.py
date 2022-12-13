"""
Измените 3 любых прошлых домашних задач, используя конструкцию try/except

"""


def main():
    """Точка входа"""
    try:
        print({"1": "Monday",
               "2": "Tuesday",
               "3": "Wednesday",
               "4": "Thursday",
               "5": "Friday",
               "6": "Saturday",
               "7": "Sunday"
            }[input("Enter the number: ")])

    except KeyError:
        print("That’s not a day of the week")


if __name__ == '__main__':
    main()
