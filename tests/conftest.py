import pytest

from src.categories import Category
from src.products import Product


@pytest.fixture
def test_product_1():
    return Product(
        name="некий товар",
        description="некий товар удивит вас",
        price=9.11,
        quantity=3
    )


@pytest.fixture
def test_product_2():
    return Product(
        name="некий другой товар",
        description="другой товар озадачит вас",
        price=1.12,
        quantity=5
    )


@pytest.fixture
def test_product_3():
    return Product(
        name="опять другой товар",
        description="опять товар не задержит вас",
        price=3.14,
        quantity=1
    )


@pytest.fixture
def product_in_dict_1():
    return {"name": "Кот", "description": "Кот в мешке", "price": 4.0,
            "quantity": 1}


@pytest.fixture
def product_in_dict_2():
    return {"name": "Мышь", "description": "Мышь в мешке", "price": 2.0,
            "quantity": 1}


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


@pytest.fixture
def test_category_3():
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
                          5)])
