def my_calculate_tax(
        price: float,
        tax_rate: float,
        discount: float = 0
) -> float:
    """Функция вычисляет стоимость товара с учетом налога и скидки.
    Скидка берется от цены с учетом налога.
    """

    for arg in [price, tax_rate, discount]:
        if not isinstance(arg, (int | float)):
            raise TypeError("Некорректный тип данных")

    if price < 0:
        raise ValueError("Неверная цена")

    if tax_rate >= 100 or tax_rate < 0:
        raise ValueError("Неверный налоговый процент")

    price_with_tax = price + (price * tax_rate / 100)
    price_with_discount = price_with_tax - price_with_tax / 100 * discount

    return round(price_with_discount, 2)
