import pytest

from src.my_function import my_calculate_tax


@pytest.mark.parametrize("price, tax_rate, result",
                         [
                             (1, 10, 1.1),
                             (20.20, 11.1, 22.4422000000),
                             (0, 10, 0),
                         ])
def test_calculate_tax(price, tax_rate, result):
    assert my_calculate_tax(price, tax_rate) == result


def test_price_errors():
    with pytest.raises(ValueError) as info_exception:
        my_calculate_tax(-10, 10)
    assert str(info_exception.value) == "Неверная цена"


def test_tax_rate_errors():
    with pytest.raises(ValueError) as info_exception:
        my_calculate_tax(100, -10)
    assert str(info_exception.value) == "Неверный налоговый процент"


def test_big_tax_rate_errors():
    with pytest.raises(ValueError) as info_exc:
        my_calculate_tax(100, 100)
    assert str(info_exc.value) == "Неверный налоговый процент"
