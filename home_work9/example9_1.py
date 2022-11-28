def kcal(f, c):
    print(f"Каллории от жиров: = {f * 9:.2f}\n"
        f"Каллории от углеводов: = {c * 4:.2f}\n"
        f"Общее количество калорий: = {((f * 9) + (c * 4)):.2f}")


if __name__ == '__main__':
    try:
        fat = float(input("Граммы жиров = "))
        carbohydrates = float(input("Граммы углеводов = "))
        if fat == 0 or carbohydrates == 0:
            raise Exception
        kcal(fat, carbohydrates)
    except ValueError:
        print('Вы ввели буквы, а не числа.\nБудьте внимательней.\nПопробуйте снова.')
    except Exception:
        print('Вы ввели ноль (0).\nПопробуйте снова.')
