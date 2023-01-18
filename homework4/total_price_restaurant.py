"""
Задача 1

Программа, которую вы напишете, должна начинаться с запроса у пользователя суммы заказа в ресторане. После этого должен
быть произведен расчет налога и  чаевых официанту.  В качестве чаевых мы оставим 18 % от стоимости заказа без учета налога.
Налог: 4%. На выходе программа должна отобразить отдельно налог, сумму чаевых и итог.

"""


def calculate_tips(order_price: float) -> dict:
    """
    Функция рассчитывает налог? чаевые и итоговую сумму
    :param order_price: сумма заказа
    :return: dict
    """
    tax = float(round(order_price * 0.18, 2))
    tips = float(round(order_price * 0.04, 2))
    total = float(round(order_price + tax + tips, 2))
    return {"tips": tips, "tax": tax, "total": total}


def main() -> None:
    """Точка входа"""
    order_price: float = float(input("Какова сумма вашего заказа: "))
    total_price = calculate_tips(order_price)
    print("Сумма чаевых: ", total_price["tips"])
    print("Налог: ", total_price["tax"])
    print("Итого сумма заказа составила: ", total_price["total"])


if __name__ == '__main__':
    main()