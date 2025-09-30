from src.products import Product


def test_products_init(first_product):
    assert first_product.name == "Bread"
    assert first_product.description == "local"
    assert first_product.price == 5.8
    assert first_product.quantity == 2

def test_new_product(dictionary1, dictionary2, dictionary3,dictionary4):
    product_list = []
    product1 = Product.new_product(dictionary1, product_list)
    product2 = Product.new_product(dictionary2, product_list)
    product3 = Product.new_product(dictionary3, product_list)
    product4 = Product.new_product(dictionary4, product_list)
    assert product1.name == "Cucumber"
    assert product1.description == "Very tasty"
    assert product1.price == 2345.5
    assert product1.quantity == 20

    assert product2.name == "Apple"
    assert product3.price == 213.5
    assert product4.quantity == 20

