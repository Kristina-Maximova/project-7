


def test_orders_init(test_order1):
    """ Тест на работу конструктора категории """
    assert test_order1.name == "Смартфоны"
    assert len(test_order1.products) == 2

def test_orders_str(test_order1):
    """ Проверка строкового отображения объекта класса orders"""
    assert str(test_order1) == "Смартфоны: заказов 2 на сумму 570000.0 руб."

def test_add_product(test_order1, test_product_1):
    """ Проверка на добавление продукта в заказ"""
    test_order1.add_product(test_product_1)
    assert len(test_order1.products) == 3

def test_custom_exception(capsys, test_lawn_grass_1, test_order1):
    """ Обработка ошибки добавления продукта с нулевым количеством """
    assert len(test_order1.products) == 2
    test_lawn_grass_1.quantity = 0
    test_order1.add_product(test_lawn_grass_1)
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-2] == "Количество добавляемого продукта не может быть нулевым"
    assert message.out.strip().split("\n")[-1] == "Обработка добавления товара завершена"