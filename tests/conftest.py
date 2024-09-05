import pytest


@pytest.fixture
def prices():
    return [100, 230]


@pytest.fixture
def taxed_prices():
    return [150, 345]