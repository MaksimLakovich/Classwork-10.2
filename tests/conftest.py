import pytest


@pytest.fixture
def prices_fixture():
    return [100, 230]


@pytest.fixture
def taxed_prices_fixture():
    return [150, 345]