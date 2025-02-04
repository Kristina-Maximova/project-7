from unittest.mock import patch
from src.products import Product


def test_product_init(test_product_1):
    assert test_product_1.name == "некий товар"
    assert test_product_1.description == "некий товар удивит вас"
    assert test_product_1.price == 9.11
    assert test_product_1.quantity == 3


def test_price_property(test_product_2):
    assert test_product_2.price == 1.12


def test_price_setter_null_price(test_product_1, capsys):
    test_product_1.price = 0
    message = capsys.readouterr()
    assert message.out == 'Цена не должна быть нулевая или отрицательная\n'


@patch("builtins.input", side_effect=["y"])
def test_price_setter_normal(mock_input, test_product_2):
    test_product_2.price = 112
    assert test_product_2.price == 112
    mock_input.asssert_called_once()


@patch("builtins.input", side_effect=["n"])
def test_price_setter_low_price(mock_input, test_product_2):
    test_product_2.price = 0.12
    assert test_product_2.price == 1.12
    mock_input.asssert_called_once()


def test_new_product(product_in_dict_1):
    new_product = Product.new_product(product_in_dict_1)
    assert new_product.name == "Кот"
    assert new_product.description == "Кот в мешке"
    assert new_product.price == 4.0
    assert new_product.quantity == 1


def test_new_product_check_in_list(product_in_dict_1, product_in_dict_2):
    my_products = []
    product_1 = Product.new_product(product_in_dict_1)
    my_products.append(product_1)
    any_new_product = Product.new_product(product_in_dict_1, my_products)
    product_2 = Product.new_product(product_in_dict_2, my_products)
    assert any_new_product not in my_products
    assert product_1.quantity == 2
    assert product_2.name == "Мышь"
    assert product_2.price == 2.0
    assert product_2.description == "Мышь в мешке"
    assert product_2.quantity == 1
