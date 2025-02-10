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
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        """ Настройка строкового отображения,
        применяется в print() и str()"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(other) is self.__class__:
            return (self.__price * self.quantity) + (other.__price * other.quantity)
        else:
            raise TypeError("Складывать между собой можно только продукты одного класса")


    @property
    def price(self) -> float:
        """ Геттер для получения прайса"""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """ Сеттер для изменения прайса"""
        if new_price > 0:
            if new_price < self.__price:
                confirm = input("y/n: ")
                if confirm.lower() == "y":
                    self.__price = new_price
            else:
                self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")

    @classmethod
    def new_product(cls, new_product: dict, products: list = None):
        """ Класс-метод для добавления нового продукта"""
        if products is not None:
            for product in products:
                if new_product["name"] == product.name:
                    product.quantity += new_product["quantity"]
                    if product.price < new_product["price"]:
                        product.price = new_product["price"]
                else:
                    cls_product = cls(new_product["name"],
                                      new_product["description"],
                                      new_product["price"],
                                      new_product["quantity"])
                    products.append(cls_product)

                    return cls_product
        else:
            return cls(new_product["name"],
                       new_product["description"],
                       new_product["price"],
                       new_product["quantity"])


if __name__ == "__main__":  # pragma: no cover.
    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5})
    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)
