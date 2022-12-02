def calculate_kkal(fat, carb):
    print(f"Калории от жиров: {fat * 9}")
    print(f"Калории от углеводов: {carb * 4}")
    print(f"Всего калорий в день: {fat * 9 + carb * 4}")


if __name__ == '__main__':
    try:
        fat = int(input("Введите количество граммов жиров: "))
        carb = int(input("Введите количество граммов углеводов: "))
    except ValueError:
        print("Ошибка!")
    else:
        calculate_kkal(fat, carb)
