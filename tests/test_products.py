from src.products import Product


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
