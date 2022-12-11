"""
Задача 1

Программа, которую вы напишете, должна начинаться с запроса у пользователя суммы заказа в ресторане. После этого
должен быть произведен расчет налога и чаевых официанту.  В качестве чаевых мы оставим 18 % от стоимости заказа без
учета налога. Налог: 4%. На выходе программа должна отобразить отдельно налог, сумму чаевых и итог.
"""

from typing import Union, TypedDict


class TotalPrice(TypedDict):
    tips: float
    tax: float
    total: float


def calculate_total_price(order_price: Union[int, float]) -> TotalPrice:
    """
    Функция рассчитывает налог, чаевые и итоговую сумму

    :param order_price: Сумма заказа в ресторане
    :return: TotalPrice
    """
    tips = order_price * 0.18
    tax = order_price * 0.04
    total = order_price + tax + tips
    return {"tips": tips, "tax": tax, "total": total}


def main() -> None:
    """ Точка входа """
    order_price: float = float(input("Введите сумму заказа: "))
    data_for_client = calculate_total_price(order_price)
    print("\nСумма заказа: ", order_price)
    print("Налог составил: %.2f" % data_for_client["tax"])
    print("Чаевые:  %.2f" % data_for_client["tips"])
    print("\nИтоговая сумма составила: %.2f" % data_for_client["total"])


if __name__ == '__main__':
    main()
