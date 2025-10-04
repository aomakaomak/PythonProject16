import builtins

import pytest

from src.categories import Category, MyList
from src.products import LawnGrass, Product, Smartphone


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


@pytest.fixture
def second_product():
    return Product(name="Butter", description="local", price=15, quantity=14)


@pytest.fixture
def wrong_product():
    return "Banana"


@pytest.fixture
def dictionary1():
    return {
        "name": "Cucumber",
        "description": "Very tasty",
        "price": 10.5,
        "quantity": 10,
    }


@pytest.fixture
def dictionary2():
    return {
        "name": "Apple",
        "description": "Very tasty",
        "price": 233.5,
        "quantity": 30,
    }


@pytest.fixture
def dictionary3():
    return {
        "name": "Orange",
        "description": "Very tasty",
        "price": 213.5,
        "quantity": 120,
    }


@pytest.fixture
def dictionary4():
    return {
        "name": "Cucumber",
        "description": "Very tasty",
        "price": 2345.5,
        "quantity": 10,
    }


@pytest.fixture
def price1():
    return 3000


@pytest.fixture
def price2():
    return 2500


@pytest.fixture
def price3():
    return 0


@pytest.fixture
def price4():
    return -34


@pytest.fixture
def set_fake_input(monkeypatch):
    def _set(ans: str):
        def _fake(prompt=""):
            print(prompt, end="")
            return ans

        monkeypatch.setattr(builtins, "input", _fake)

    return _set


@pytest.fixture
def smart_product1():
    return Smartphone(
        name="Samsung S20FE",
        description="local",
        price=700,
        quantity=10,
        efficiency="A",
        model="S20FE",
        memory=64,
        color="white",
    )


@pytest.fixture
def smart_product2():
    return Smartphone(
        name="Samsung A110",
        description="local",
        price=400,
        quantity=30,
        efficiency="B",
        model="A110",
        memory=16,
        color="black",
    )


@pytest.fixture
def grass_product1():
    return LawnGrass(
        name="Grass",
        description="local",
        price=100,
        quantity=200,
        country="China",
        germination_period=2,
        color="green",
    )


@pytest.fixture
def dictionary5():
    return {
        "name": "Cucumber",
        "description": "Very tasty",
        "price": 10.5,
        "quantity": 10,
        "efficiency": 20,
        "model": "Samsung",
        "memory": 64,
        "color": "white",
    }


@pytest.fixture
def dictionary6():
    return {
        "name": "Apple",
        "description": "Very tasty",
        "price": 233.5,
        "quantity": 30,
        "efficiency": 30,
        "model": "Xiaomi",
        "memory": 32,
        "color": "black",
    }


@pytest.fixture
def dictionary7():
    return {
        "name": "Orange",
        "description": "Very tasty",
        "price": 213.5,
        "quantity": 120,
        "country": "China",
        "germination_period": 1,
        "color": "green",
    }


@pytest.fixture
def dictionary8():
    return {
        "name": "Cucumber",
        "description": "Very tasty",
        "price": 2345.5,
        "quantity": 10,
        "country": "China",
        "germination_period": 3,
        "color": "blue",
    }
