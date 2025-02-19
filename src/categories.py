from src.products import Product
from src.base_product import BaseCategory
from src.my_exception import ZeroQuantityException


class Category(BaseCategory):
    """ Класс для создания категорий"""
    name: str
    description: str
    products: list  # д.б. список объектов класса Product

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        """ Конструктор класса категорий"""
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        """ Задает строковое отображение продукта"""
        return f"{self.name}, количество продуктов: {len(self.get_product_list)} шт."

    def add_product(self, product: Product) -> None:
        """ Добавление объекта класса Product в приватный список продуктов"""
        if not isinstance(product, Product):
            raise TypeError("Добавлять можно только объекты классов Product и дочерних от него.")
        try:
            if product.quantity == 0:
                raise ZeroQuantityException("Количество добавляемого продукта не может быть нулевым")
        except ZeroQuantityException as e:
            print(str(e))
        else:
            self.__products.append(product)
            Category.product_count += 1
            print("Товар добавлен")
        finally:
            print("Обработка добавления товара завершена")

    @property
    def products(self) -> str:
        """Геттер для получения строки с продуктами"""
        product_line = ""
        for product in self.__products:
            product_line += f"{str(product)}\n"
        return product_line

    @property
    def get_product_list(self):
        """ Геттер для получения списка продуктов"""
        my_list = []
        for product in self.__products:
            my_list.append(product)
        return my_list

    def middle_price(self):
        try:
            return round(sum([product.quantity for product in self.__products]) / len(self.__products),2)
        except ZeroDivisionError:
            return 0


if __name__ == "__main__":  # pragma: no cover.
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])
    print(category1.get_product_list[0])
    print(category1.middle_price())

    category_none_products = Category("Телевизоры",
                                      "Современный телевизор, который позволяет наслаждаться просмотром", [])
    print(category_none_products.middle_price())
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print(category1.products)
