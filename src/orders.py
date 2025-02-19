from src.base_product import BaseCategory
from src.products import Product


class Order(BaseCategory):
    orders_list = []

    def __init__(self, product: Product, quantity: int = 0):
        self.product = product
        self.quantity = quantity
        self.cost = self.product.price * self.quantity
        Order.orders_list.append(self)

    def __str__(self):
        return f"Заказ: {self.product.name} в количестве {self.quantity}шт., на сумму {self.cost}руб."

    def add_product(self, booked_product, quantity):
        if not isinstance(booked_product, Product):
            raise TypeError("Заказ можно оформить только на объекты классов Product и дочерних от него.")
        elif self.quantity > booked_product.quantity:
            print("Количество в заказе превышает количество товара на складе")
        else:
            return Order(booked_product, quantity)


if __name__ == '__main__':  # pragma: no cover.

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    my_order = Order(product1, 2)
    order1 = Order(product2, 1)
    order2 = my_order.add_product(product3, 1)

    print(my_order)

    print(Order.orders_list[0])
    print(Order.orders_list[1])
    print(Order.orders_list[2])
