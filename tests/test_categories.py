def test_category_init(test_category_1, test_category_2):
    assert test_category_1.name == "некая категория"
    assert test_category_1.description == "Это расширит ваши возможности"

    assert test_category_1.category_count == 2
    assert test_category_2.category_count == 2

    assert test_category_1.product_count == 5
    assert test_category_2.product_count == 5


def test_add_product(test_category_3, test_product_3):
    test_category_3.add_product(test_product_3)
    assert test_category_3.products == (
        'некий товар, 9.11 руб. Остаток: 3 шт.\n'
        'некий другой товар, 1.12 руб. Остаток: 5 шт.\n'
        'опять другой товар, 3.14 руб. Остаток: 1 шт.\n'
    )
    # assert test_category_3.product_count == 3


def test_products(test_category_1):
    assert test_category_1.products == (
        'некий товар, 9.11 руб. Остаток: 3 шт.\n'
        'некий другой товар, 1.12 руб. Остаток: 5 шт.\n')


def test_category_str(test_category_1):
    assert str(test_category_1) == "некая категория, количество продуктов: 2 шт."


def test_get_product_list(test_category_2):
    assert len(test_category_2.get_product_list) == 3
