import json
import os
from typing import Any

from categories import Category
from products import Product


def read_file(file_path: str) -> list:
    """ Читаем файл """
    full_path = os.path.abspath(file_path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


def create_objects_from_json(data: list) -> Any:
    """ Формируем данные """
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))

    return categories


# if __name__ == "__main__":
#     data = read_file("data/products.json")
#     print(data)
#     print(type(data))
#
#     result = create_objects_from_json(data)
#     print(result)
#     print(result[0].name)
#     print(result[0].description)
#     print(result[0].products)
