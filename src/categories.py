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


# if __name__ == "__main__":

