class Product:
    """ Класс для создания продукта"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity=0):
        """ Конструктор продуктов, или инициализация класса """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
