def calories(a, b):
    print(f"Calories from fat: {a*9}")
    print(f"Calories from carbohydrates: {b*4}")
    print(f"Total number of calories: {a*9+b*4}")


if __name__ == '__main__':
    try:
        fat = int(input("Amount of consumed fat: "))
        carb = int(input("Amount of consumed carbohydrates: "))
    except ValueError:
        print("Error")
    else:
        calories(fat, carb)
