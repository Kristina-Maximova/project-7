from src.products import Product


class Smartphone(Product):
    name: str
    efficiency: str
    model: str
    memory: str
    color: str
    description: str
    price: float
    quantity: int
    def __init__(self, name, efficiency, model, memory, color,
                 description, price, quantity=0):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

