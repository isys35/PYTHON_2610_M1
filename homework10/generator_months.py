# 4 Генератор месяцев
# Напишите программу, в которой используется функция-генератор, создающая итерируемый объект с названиями месяцев

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']


def gen(list_months):
    for month in list_months:
        yield month


if __name__ == '__main__':
    # принтим наш обьект чтобы убедиться что это генератор
    print(gen(months))
    gen = gen(months)
    for item in gen:
        print(item)

