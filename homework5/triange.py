side_a = float(input("Введите длину стороны a треугольника: "))
side_b = float(input("Введите длину стороны b треугольника: "))
side_c = float(input("Введите длину стороны c треугольника: "))

if 0 < side_c < (side_a + side_b) and \
        0 < side_a < (side_b + side_c) and \
        0 < side_b < (side_c + side_a):
    print("\nТакой треугольник может существовать")
else:
    print("\nТакой треугольник НЕ может существовать.")
