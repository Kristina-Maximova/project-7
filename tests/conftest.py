import pytest

from src.products import Product
from src.categories import Category


@pytest.fixture
def test_product():
    return Product(
        name="некий товар",
        description="некий товар удивит вас",
        price=9.11,
        quantity=3
    )


@pytest.fixture
def test_category():
    return Category(
        name="некая категория",
        description="Это расширит ваши возможности",
        products=[Product_1("некий товар",
                            "некий товар удивит вас",
                            9.11,
                            3),
                  Product_2("некий другой товар",
                            "другой товар озадачит вас",
                            1.12,
                            5)]
    )
