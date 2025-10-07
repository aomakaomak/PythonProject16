import pytest

from src.products import LawnGrass, Product, Smartphone


def test_products_init(first_product):
    assert first_product.name == "Bread"
    assert first_product.description == "local"
    assert first_product.price == 5.8
    assert first_product.quantity == 2


def test_new_product(dictionary1, dictionary2, dictionary3, dictionary4):
    product1 = Product.new_product(dictionary1)
    product2 = Product.new_product(dictionary2)
    product3 = Product.new_product(dictionary3)
    product4 = Product.new_product(dictionary4)
    assert product1.name == "Cucumber"
    assert product1.description == "Very tasty"
    assert product1.price == 10.5
    assert product1.quantity == 10

    assert product2.name == "Apple"
    assert product3.price == 213.5
    assert product4.quantity == 10


# !!! На геттер price(self)  отдельно тест смысла писать нет, поскольку
# он уже фактически реализован в test_products_init -- если бы геттер не работал, то и
# test_products_init упал бы, так как мы сделали price приватным


def test_price_setter(
    first_product, price1, price2, price3, price4, set_fake_input, capsys
):
    first_product.price = price1
    assert first_product.price == 3000

    set_fake_input("n")
    first_product.price = price2
    out = capsys.readouterr().out
    assert "Подтвердите цену" in out
    assert first_product.price == 3000

    first_product.price = price3
    out = capsys.readouterr().out
    assert "не должна быть нулевая" in out
    assert first_product.price == 3000

    first_product.price = price4
    out = capsys.readouterr().out
    assert "не должна быть нулевая" in out
    assert first_product.price == 3000

    set_fake_input("y")
    first_product.price = 2500
    out = capsys.readouterr().out
    assert "Подтвердите цену" in out
    assert first_product.price == 2500


def test_products_str_product(first_product, capsys):
    print(first_product)
    out, err = capsys.readouterr()
    assert "Bread, 5.8 руб. Остаток: 2 шт." in out


def test_products_add_product(first_product, second_product):
    assert (first_product + second_product) == 221.6


def test_products_add_wrong_product(first_product, wrong_product):
    expected_message = f"Ожидался Product, а получен {type(wrong_product).__name__}"
    with pytest.raises(TypeError) as excinfo:
        _ = first_product + wrong_product
    assert str(excinfo.value) == expected_message


def test_products_of_subclass_init(smart_product1):
    assert smart_product1.name == "Samsung S20FE"
    assert smart_product1.description == "local"
    assert smart_product1.price == 700
    assert smart_product1.quantity == 10
    assert smart_product1.efficiency == "A"
    assert smart_product1.model == "S20FE"
    assert smart_product1.memory == 64
    assert smart_product1.color == "white"


def test_new_product_of_subclass(dictionary5, dictionary6, dictionary7, dictionary8):
    product1 = Smartphone.new_product(dictionary5)
    product2 = Smartphone.new_product(dictionary6)
    product3 = LawnGrass.new_product(dictionary7)
    product4 = LawnGrass.new_product(dictionary8)
    assert product1.name == "Cucumber"
    assert product1.description == "Very tasty"
    assert product1.price == 10.5
    assert product1.quantity == 10
    assert product1.efficiency == 20
    assert product1.model == "Samsung"
    assert product1.memory == 64
    assert product1.color == "white"

    assert product2.model == "Xiaomi"
    assert product3.germination_period == 1
    assert product4.color == "blue"


def test_products_add_product_of_same_subclass(smart_product1, smart_product2):
    assert (smart_product1 + smart_product2) == 19000


def test_products_add_product_of_another_subclass(smart_product1, grass_product1):
    expected_message = "Это продукты разных классов"
    with pytest.raises(TypeError) as excinfo:
        _ = smart_product1 + grass_product1
    assert str(excinfo.value) == expected_message


def test_products_zero_quantity():
    expected_message = "Товар с нулевым количеством не может быть добавлен"
    with pytest.raises(ValueError) as excinfo:
        _ = Product("Cucumber", "Very tasty", 23.5, 0)
    assert str(excinfo.value) == expected_message
