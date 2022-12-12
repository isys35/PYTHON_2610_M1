def fats():
    a = int(input("Сколько граммов жиров вы употребили за день: "))
    calories_from_fats = a * 9
    return f"Количество калорий от жиров: {calories_from_fats}"


def carbohydrates():
    b = int(input("Сколько граммов углеводов вы употребили за день: "))
    calories_from_carbohydrates = b * 4
    return f"Количество калорий от углеводов: {calories_from_carbohydrates}"


if __name__ == '__main__':
    print(f"{fats()}\n{carbohydrates()}")
