import pytest

from src.my_function import my_calculate_tax


@pytest.mark.parametrize("price, tax_rate, result",
                         [
                             (20.20, 11.1, 22.44),
                             (0, 10, 0),
                         ])
def test_calculate_tax(price, tax_rate, result):
    assert my_calculate_tax(price, tax_rate) == result


@pytest.mark.parametrize("price, tax_rate, discount, result",
                         [
                             (1, 10, 50, 0.55),
                             (100, 20, 25, 90),
                         ])
def test_with_discount(price, tax_rate, discount, result):
    assert my_calculate_tax(price, tax_rate, discount) == result


def test_without_discount():
    assert my_calculate_tax(100, 20) == 120


def test_price_errors():
    with pytest.raises(ValueError) as info_exception:
        my_calculate_tax(-10, 10)
    assert str(info_exception.value) == "Неверная цена"


def test_tax_rate_errors():
    with pytest.raises(ValueError) as info_exception:
        my_calculate_tax(100, -10)
    assert str(info_exception.value) == "Неверный налоговый процент"


def test_big_tax_rate_errors():
    with pytest.raises(ValueError) as info_exception:
        my_calculate_tax(100, 100)
    assert str(info_exception.value) == "Неверный налоговый процент"


def test_wrong_type():
    with pytest.raises(TypeError) as info_exception:
        my_calculate_tax("500", "25", "15")
    assert str(info_exception.value) == "Некорректный тип данных"
