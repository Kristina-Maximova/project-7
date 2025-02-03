import json
import os

from src.products import Product
from src.categories import Category


def read_json(path: str) -> list:
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="utf-8") as file:
        data = json.load(file)
        return data



if __name__ == "__main__":
    my_data = read_json("../data/products.json")
    print(my_data)