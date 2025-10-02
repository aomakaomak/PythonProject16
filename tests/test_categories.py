from src.categories import MyList


def test_categories_init(first_category, second_category):
    assert first_category.name == "Vegetables"
    assert first_category.description == "Fresh"
    assert second_category.name == "Fruits"
    assert second_category.description == "Tasty"

    assert first_category.number_of_categories == 2
    assert second_category.number_of_categories == 2

    assert first_category.number_of_products == 5
    assert second_category.number_of_products == 5


def test_categories_products_property(first_category):
    assert first_category.products == (
        "Cucumber, 23.5 руб. Остаток: 10 шт.\n" "Tomato, 45.2 руб. Остаток: 20 шт."
    )


def test_categories_add_product(first_category, first_product):
    assert len(first_category.products_in_list) == 2
    first_category.add_product(first_product)
    assert first_category.products == (
        "Cucumber, 23.5 руб. Остаток: 10 шт.\n"
        "Tomato, 45.2 руб. Остаток: 20 шт.\n"
        "Bread, 5.8 руб. Остаток: 2 шт."
    )
    assert len(first_category.products_in_list) == 3


def test_categories_str_category(first_category, capsys):
    print(first_category)
    out, err = capsys.readouterr()
    assert "Vegetables, количество продуктов: 30 шт." in out


def test_categories_class_mylist(first_category, capsys):
    category = MyList(first_category)
    for product in category:
        print(product)
    out, err = capsys.readouterr()
    assert (
        "Cucumber, 23.5 руб. Остаток: 10 шт.\nTomato, 45.2 руб. Остаток: 20 шт." in out
    )
