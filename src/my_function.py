def my_calculate_tax(price: float, tax_rate: float) -> float:
    """Функция вычисляет стоимость товара с учетом налога"""

    if price < 0:
        raise ValueError("Неверная цена")

    if tax_rate >= 100 or tax_rate < 0:
        raise ValueError("Неверный налоговый процент")

    return price + (price * tax_rate / 100)
