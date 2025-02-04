from src.products import Product


class Category:
    """ Класс для создания категорий"""
    name: str
    description: str
    products: list  # д.б. список объектов класса Product

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product) -> None:
        """ Добавление объекта класса Product в приватный список продуктов"""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Геттер для получения строки с продуктами"""
        product_line = ""
        for product in self.__products:
            product_line += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return product_line

    # @add_product.setter
    # def add_product(self, product) -> None:
    #     """ Добавление объекта класса Product в приватный список продуктов"""
    #     self.__products.append(product)
    #     Category.product_count += 1


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(category1.products)
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print(category1.products)
    print(category1.product_count)
