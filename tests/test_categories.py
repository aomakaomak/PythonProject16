

def test_categories_init(first_category, second_category):
    assert first_category.name == "Vegetables"
    assert first_category.description == "Fresh"
    assert second_category.name == "Fruits"
    assert second_category.description == "Tasty"

    assert first_category.number_of_categories == 2
    assert second_category.number_of_categories == 2

    assert first_category.number_of_products == 5
    assert second_category.number_of_products == 5
