def my_calculate_tax(price: float, tax_rate: float) -> float:
    """Функция вычисляет стоимость товара с учетом налога"""

    if price < 0:
        raise ValueError("Неверная цена")

    return price + (price * tax_rate / 100)
