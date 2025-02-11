def test_lawn_grass_init(test_lawn_grass_1):
    """ Проверка работы конструктора класса LawnGrass """
    assert test_lawn_grass_1.name == "Газонная трава"
    assert test_lawn_grass_1.country == "Россия"
    assert test_lawn_grass_1.germination_period == "7 дней"
    assert test_lawn_grass_1.color == "Зеленый"
    assert test_lawn_grass_1.description == "Элитная трава для газона"
    assert test_lawn_grass_1.price == 500.0
    assert test_lawn_grass_1.quantity == 20
