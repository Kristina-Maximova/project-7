from src.products import Product


class LawnGrass(Product):
    """ Класс газонной травы как продукта"""
    name: str
    country: str
    germination_period: str
    color: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        """ Конструктор класса газонной травы как продукта"""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


if __name__ == "__main__":  # pragma: no cover
    data_for_new_lawn_grass = {
        'name': 'травушка',
        'description': 'муравушка',
        'price': 2555,
        'quantity': 50,
        'country': "Ирландия",
        'germination_period': '3 года',
        'color': 'салатовый'
    }

    # Как отработает метод new_product из родительского класса:
    my_new_amazing_lawn_grass = LawnGrass.new_product(data_for_new_lawn_grass)
    print(my_new_amazing_lawn_grass.color)
