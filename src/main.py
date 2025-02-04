from src.categories import Category
from src.products import Product

if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)  # pragma: no cover
    print(product1.description)  # pragma: no cover
    print(product1.price)  # pragma: no cover
    print(product1.quantity)  # pragma: no cover

    print(product2.name)  # pragma: no cover
    print(product2.description)  # pragma: no cover
    print(product2.price)  # pragma: no cover
    print(product2.quantity)  # pragma: no cover

    print(product3.name)  # pragma: no cover
    print(product3.description)  # pragma: no cover
    print(product3.price)  # pragma: no cover
    print(product3.quantity)  # pragma: no cover

    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, "
                         "но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])

    print(category1.name == "Смартфоны")  # pragma: no cover
    print(category1.description)  # pragma: no cover
    print(len(category1.products))  # pragma: no cover
    print(category1.category_count)  # pragma: no cover
    print(category1.product_count)  # pragma: no cover

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры",
                         "Современный телевизор, "
                         "который позволяет наслаждаться просмотром, "
                         "станет вашим другом и помощником",
                         [product4])

    print(category2.name)  # pragma: no cover
    print(category2.description)  # pragma: no cover
    print(len(category2.products))  # pragma: no cover
    print(category2.products)  # pragma: no cover

    print(Category.category_count)  # pragma: no cover
    print(Category.product_count)  # pragma: no cover
