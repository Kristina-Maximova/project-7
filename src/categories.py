from src.products import Product


class Category:
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
            raise TypeError("Добавлять можно только объекты классов Product и дочерних от него ")
        self.__products.append(product)
        Category.product_count += 1

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

# if __name__ == "__main__":
