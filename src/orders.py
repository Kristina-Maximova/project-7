from src.base_product import BaseCategory
from src.my_exception import ZeroQuantityException
from src.products import Product


class Order(BaseCategory):
    """ Класс для формирования заказов"""

    products: list[Product]

    def __init__(self, name: str, products: list):
        """
        Конструктор класса заказов
        :param name: наименование категории продуктов
        :param products: Список объектов класса продукт
        """
        self.name = name
        self.products = products

    def __str__(self):
        order_cost = sum((product.price * product.quantity) for product in self.products)
        return f"{self.name}: заказов {len(self.products)} на сумму {order_cost} руб."

    def add_product(self, booked_product):
        if not isinstance(booked_product, Product):
            raise TypeError("Заказ можно оформить только на объекты классов Product и дочерних от него.")
        try:
            if booked_product.quantity == 0:
                raise ZeroQuantityException("Количество добавляемого продукта не может быть нулевым")
        except ZeroQuantityException as e:
            print(str(e))
        else:
            self.products.append(booked_product)
            print("Товар добавлен в заказ")
        finally:
            print("Обработка добавления товара завершена")


if __name__ == '__main__':  # pragma: no cover.

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    my_order = Order("Смартфоны", [product1, ])
    my_order.add_product(product2)
    print(my_order)
