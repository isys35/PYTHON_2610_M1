def kcal(fat, carbohydrates):
    print(f"Каллории от жиров: = {fat * 9:.2f}\n"
        f"Каллории от углеводов: = {carbohydrates * 4:.2f}\n"
        f"Общее количество калорий: = {((fat * 9) + (carbohydrates * 4)):.2f}")


if __name__ == '__main__':
    try:
        user_fat = float(input("Граммы жиров = "))
        user_carbohydrates = float(input("Граммы углеводов = "))
        if user_fat == 0 or user_carbohydrates == 0:
            raise Exception
        kcal(user_fat, user_carbohydrates)
    except ValueError:
        print('Вы ввели буквы, а не числа.\nБудьте внимательней.\nПопробуйте снова.')
    except Exception:
        print('Вы ввели ноль (0).\nПопробуйте снова.')
