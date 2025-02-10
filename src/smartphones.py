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
    efficiency: float
    model: str
    memory: int
    color: str
    def __init__(self, name, description, price, quantity,
                 efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

