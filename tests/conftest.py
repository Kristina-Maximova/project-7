import pytest

from src.categories import Category
from src.lawn_grass import LawnGrass
from src.products import Product
from src.products_iterator import ProductsIterator
from src.smartphones import Smartphone


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


@pytest.fixture
def test_product_iterator(test_category_2):
    return ProductsIterator(test_category_2)


@pytest.fixture
def test_smartphone1():
    return Smartphone("Samsung Galaxy S23 Ultra",
                      "256GB, Серый цвет, 200MP камера",
                      180000.0,
                      5,
                      95.5,
                      "S23 Ultra",
                      256,
                      "Серый")


@pytest.fixture
def test_smartphone2():
    return Smartphone("Iphone 15",
                      "512GB, Gray space",
                      210000.0,
                      8,
                      98.2,
                      "15",
                      512,
                      "Gray space")


@pytest.fixture
def test_lawn_grass_1():
    return LawnGrass("Газонная трава",
                     "Элитная трава для газона",
                     500.0,
                     20,
                     "Россия",
                     "7 дней",
                     "Зеленый")


@pytest.fixture
def test_lawn_grass_2():
    return LawnGrass("Газонная трава 2",
                     "Выносливая трава",
                     450.0,
                     15,
                     "США",
                     "5 дней",
                     "Темно-зеленый")
