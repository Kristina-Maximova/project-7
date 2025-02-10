from src.products import Product

class LawnGrass(Product):
    name: str
    country: str
    germination_period: str
    color: str
    description: str
    price: float
    quantity: int
    def __init(self, name, country, germination_period, color, description, price, quantity=0):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

