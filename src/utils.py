import json
import os

from src.categories import Category
from src.products import Product


def read_json(path: str) -> list:
    """
    Чтение данных из json -файла
    :param path: str
    :return: list
    """
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="utf-8") as file:
        data = json.load(file)
        return data


def create_object_from_data(data: list) -> list:
    """ Создание объектов классов из списка словарей"""
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))
    return categories


if __name__ == "__main__":  # pragma: no cover.
    my_data = read_json("../data/products.json")
    # my_categories = create_object_from_data(my_data)

    print(my_data)
