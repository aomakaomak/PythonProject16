import pytest

from src.categories import Category
from src.products import Product


@pytest.fixture
def first_category():
    return Category(
        name="Vegetables",
        description="Fresh",
        products=[
            Product("Cucumber", "Very tasty", 23.5, 10),
            Product("Tomato", "Very fresh", 45.2, 20),
        ],
    )


@pytest.fixture
def second_category():
    return Category(
        name="Fruits",
        description="Tasty",
        products=[
            Product("Banana", "Yellow", 53.5, 30),
            Product("Orange", "like a ball", 115.2, 40),
            Product("Lime", "Sad", 215.2, 50),
        ],
    )


@pytest.fixture
def first_product():
    return Product(name="Bread", description="local", price=5.8, quantity=2)
