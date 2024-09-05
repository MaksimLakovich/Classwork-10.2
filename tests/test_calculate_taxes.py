import pytest

from src.main import calculate_taxes


def test_calculate_taxes_positive_case(prices, taxed_prices):
    assert calculate_taxes(prices, 50) == taxed_prices


def test_calculate_taxes_errors(prices, taxed_prices):
    with pytest.raises(ValueError) as exc_info:
        calculate_taxes(prices, -10)
    assert str(exc_info.value) == "Неверный налоговый процент"