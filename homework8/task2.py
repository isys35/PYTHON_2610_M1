"""
Задача 1

Измените 3 любых прошлых домашних задач, ипользуя контсрукцию try/except
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
    if order_price <= 0:
        raise ValueError("Сумма заказа некорректна")
    tips = order_price * 0.18
    tax = order_price * 0.04
    total = order_price + tax + tips
    return {"tips": tips, "tax": tax, "total": total}


def main() -> None:
    """ Точка входа """
    try:
        order_price: float = float(input("Введите сумму заказа: "))
        data_for_client = calculate_total_price(order_price)
        print("\nСумма заказа: ", order_price)
        print("Налог составил: %.2f" % data_for_client["tax"])
        print("Чаевые:  %.2f" % data_for_client["tips"])
        print("\nИтоговая сумма составила: %.2f" % data_for_client["total"])
    except ValueError as error_message:
        print(f"Некорректные данные для обработки: {error_message}")
    except Exception as err:
        print(f"Что-то пошло не так: {err}")


if __name__ == '__main__':
    main()
