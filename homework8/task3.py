"""
Задача 1

Измените 3 любых прошлых домашних задач, ипользуя контсрукцию try/except
"""
from decimal import Decimal, InvalidOperation


def is_triangle(side_a: Decimal, side_b: Decimal, side_c: Decimal) -> bool:
    """
    Функция проверяет, может ли существовать треугольник

    :rtype: object
    :param side_a: Первая сторона треугольника
    :param side_b: Вторая сторона треугольника
    :param side_c: Третья сторона треугольника
    :return: bool
    """

    if side_a.compare(0) == 1 and side_b.compare(0) == 1 and side_c.compare(0) == 1:
        if side_c.compare(side_a + side_b) == -1 and \
                side_a.compare(side_b + side_c) == -1 and \
                side_b.compare(side_c + side_a) == -1:
            return True
        return False
    else:
        raise ValueError("Сторона треугольника не может быть меньше или равна 0.")


def main() -> None:
    """ Точка входа """
    try:
        side_a: Decimal = Decimal(input("Введите длину стороны a треугольника: "))
        side_b: Decimal = Decimal(input("Введите длину стороны b треугольника: "))
        side_c: Decimal = Decimal(input("Введите длину стороны c треугольника: "))
        if is_triangle(side_a, side_b, side_c):
            print("\nТакой треугольник может существовать")
        else:
            print("\nТакой треугольник НЕ может существовать.")
    except InvalidOperation as error_message:
        print(f"Некорректный ввод данных. {error_message}")


if __name__ == '__main__':
    main()
