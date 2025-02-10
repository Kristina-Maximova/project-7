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

