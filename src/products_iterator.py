from src.categories import Category
from src.products import Product


class ProductsIterator:
    """ Перебор продуктов в конкретной категории"""

    def __init__(self, category_obj: Category):
        """ Конструктор итератора продуктов в категории """
        self.category = category_obj
        self.index = 0

    def __iter__(self):
        """ Возвращает итератор категории"""
        self.index = 0  # обязательно нужно обнулять индекс
        return self

    def __next__(self):
        """ Настраивает возвращение продуктов по одному,
         здесь же обрабатывается завершение цикла итерации"""
        if self.index < len(self.category.get_product_list):
            product = self.category.get_product_list[self.index]
            self.index += 1
            return product  # возвращаем объект класса Product
        else:
            raise StopIteration

    # def get_product_list(self):
    #     my_list = []
    #     for product in self.__products:
    #         my_list.append(product)
    #     return my_list


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    my_iterator = ProductsIterator(category1)
    for product in my_iterator:
        print(product)
