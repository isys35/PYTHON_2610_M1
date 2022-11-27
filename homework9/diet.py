from homework9.decorators import diet_printer


def calculate_fat_calories(fat):
    return fat * 9


def calculate_carbohydrates_calories(carbohydrates):
    return carbohydrates * 4


@diet_printer
def calculate_calories(fat, carbohydrates):
    return calculate_fat_calories(fat) + calculate_carbohydrates_calories(carbohydrates)


amount_of_fat = int(input("Enter the amount of fat eaten per day: "))
amount_of_carbohydrates = int(input("Enter the amount of carbohydrates eaten per day: "))

calculate_calories(amount_of_fat, amount_of_carbohydrates)
