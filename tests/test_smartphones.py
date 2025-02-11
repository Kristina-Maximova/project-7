def test_smartphone_init(test_smartphone1):
    """ Проверка работы конструктора класса Smartphone"""
    assert test_smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert test_smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert test_smartphone1.price == 180000.0
    assert test_smartphone1.quantity == 5
    assert test_smartphone1.efficiency == 95.5
    assert test_smartphone1.model == "S23 Ultra"
    assert test_smartphone1.memory == 256
    assert test_smartphone1.color == "Серый"
