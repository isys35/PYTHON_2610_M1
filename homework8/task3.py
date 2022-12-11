"""
Задача 1

Измените 3 любых прошлых домашних задач, ипользуя контсрукцию try/except
"""


def is_triangle(side_a: float, side_b: float, side_c: float) -> bool:
    """
    Функция проверяет, может ли существовать треугольник

    :param side_a: Первая сторона треугольника
    :param side_b: Вторая сторона треугольника
    :param side_c: Третья сторона треугольника
    :return: bool
    """
    if side_a <= 0 or side_b <= 0 or side_c <= 0:
        raise ValueError("Сторона треугольника не может быть меньше или равна 0.")
    if 0 < side_c < (side_a + side_b) and \
            0 < side_a < (side_b + side_c) and \
            0 < side_b < (side_c + side_a):
        return True
    return False


def main() -> None:
    """ Точка входа """
    try:
        side_a: float = float(input("Введите длину стороны a треугольника: "))
        side_b: float = float(input("Введите длину стороны b треугольника: "))
        side_c: float = float(input("Введите длину стороны c треугольника: "))
        if is_triangle(side_a, side_b, side_c):
            print("\nТакой треугольник может существовать")
        else:
            print("\nТакой треугольник НЕ может существовать.")
    except ValueError as error_message:
        print(f"Некорректный ввод данных. {error_message}")


if __name__ == '__main__':
    main()
