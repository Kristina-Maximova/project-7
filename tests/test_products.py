from src.products import Product


def test_product_init(test_product_1):
    assert test_product_1.name == "некий товар"
    assert test_product_1.description == "некий товар удивит вас"
    assert test_product_1.price == 9.11
    assert test_product_1.quantity == 3

