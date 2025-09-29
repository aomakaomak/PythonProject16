def test_products_init(first_product):
    assert first_product.name == "Bread"
    assert first_product.description == "local"
    assert first_product.price == 5.8
    assert first_product.quantity == 2
