import pytest

from src.main import calculate_taxes
from tests.conftest import prices_fixture, taxed_prices_fixture


@pytest.mark.parametrize("prices, taxed_prices",
                         [
                             ([100, 200, 2000], [150, 300, 3000]),
                         ])
def test_calculate_taxes_positive_case(prices, taxed_prices):
    assert calculate_taxes(prices, 50) == taxed_prices


def test_calculate_taxes_errors(prices_fixture, taxed_prices_fixture):
    with pytest.raises(ValueError) as exc_info:
        calculate_taxes(prices_fixture, -10)
    assert str(exc_info.value) == "Неверный налоговый процент"

    with pytest.raises(ValueError) as exception_info:
        calculate_taxes([0, -1], 50)
    assert str(exception_info.value) == "Неверная цена"