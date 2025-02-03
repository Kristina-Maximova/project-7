import pytest

from src.products import Product
from src.categories import Category


@pytest.fixture
def test_product_1():
    return Product(
        name="некий товар",
        description="некий товар удивит вас",
        price=9.11,
        quantity=3
    )


def test_product_2():
    return Product(
        name="некий другой товар",
        description="другой товар озадачит вас",
        price=1.12,
        quantity=5
    )


@pytest.fixture
def test_category_1():
    return Category(
        name="некая категория",
        description="Это расширит ваши возможности",
        products=[Product("некий товар",
                          "некий товар удивит вас",
                          9.11,
                          3),
                  Product("некий другой товар",
                          "другой товар озадачит вас",
                          1.12,
                          5)]
    )


@pytest.fixture
def test_category_2():
    return Category(
        name="иная категория",
        description="Это вдохновит вас",
        products=[Product("иной товар",
                          "иной товар не удивит вас",
                          0.11,
                          2),
                  Product("другой иной товар",
                          "другой иной товар не озадачит вас",
                          0.12,
                          6),
                  Product("совсем иной товар",
                          "иной товар не затруднит вас",
                          11.2,
                          8)]

    )
