import pytest


def test_products_iterator(test_product_iterator):
    """ проверка работы итератора продуктов в категории"""
    assert test_product_iterator.index == 0
    assert next(test_product_iterator).name == "иной товар"
    assert next(test_product_iterator).name == "другой иной товар"
    assert next(test_product_iterator).name == "совсем иной товар"

    with pytest.raises(StopIteration):
        next(test_product_iterator)
