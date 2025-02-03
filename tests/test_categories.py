def test_category_init(test_category_1, test_category_2):
    assert test_category_1.name == "некая категория"
    assert test_category_1.description == "Это расширит ваши возможности"
    assert len(test_category_1.products) == 2

    assert test_category_1.category_count == 2
    assert test_category_2.category_count == 2

    assert test_category_1.product_count == 5
    assert test_category_2.product_count == 5
