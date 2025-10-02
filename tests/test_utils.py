import json

import pytest

from src.utils import create_objects_from_json, read_file


def test_read_file_valid_json(tmp_path):
    """Тест корректного чтения JSON"""
    # создаём временный файл
    data = [{"name": "Test", "value": 42}]
    file_path = tmp_path / "data.json"
    file_path.write_text(json.dumps(data), encoding="utf-8")

    result = read_file(str(file_path))

    assert isinstance(result, list)
    assert result == data


def test_read_file_file_not_found():
    """Тест ошибки при отсутствии файла"""
    with pytest.raises(FileNotFoundError):
        read_file("no_such_file.json")


def test_read_file_invalid_json(tmp_path):
    """Тест ошибки при некорректном JSON"""
    file_path = tmp_path / "broken.json"
    file_path.write_text("{invalid json}", encoding="utf-8")

    with pytest.raises(json.JSONDecodeError):
        read_file(str(file_path))


def _assert_products_container(products, expected):
    """
    Унифицированная проверка содержимого products.
    expected: список словарей с полями name, description, price, quantity
    """
    if isinstance(products, list):
        # Проверяем, что это последовательность элементов с нужными атрибутами
        assert len(products) == len(expected)
        for obj, exp in zip(products, expected):
            # duck-typing: у элемента должны быть нужные атрибуты
            for attr in ("name", "description", "price", "quantity"):
                assert hasattr(obj, attr), f"Отсутствует атрибут {attr}"
            assert obj.name == exp["name"]
            assert obj.description == exp["description"]
            assert obj.price == exp["price"]
            assert obj.quantity == exp["quantity"]
    elif isinstance(products, str):
        # Строковая реализация: проверяем, что в строке есть ключевые значения
        for exp in expected:
            assert exp["name"] in products
            # не у всех строковых реализаций есть формат цены/кол-ва одинаковый,
            # поэтому проверяем только наличие чисел в виде подстрок
            assert str(exp["price"]) in products
            assert str(exp["quantity"]) in products
    else:
        pytest.fail(f"Неожиданный тип products: {type(products)!r}")


def test_create_objects_from_json_valid():
    """Тест корректного преобразования JSON-данных (список или строка допустимы)."""
    data = [
        {
            "name": "Fruits",
            "description": "Sweet and tasty",
            "products": [
                {"name": "Apple", "description": "Red", "price": 10.5, "quantity": 5},
                {
                    "name": "Banana",
                    "description": "Yellow",
                    "price": 7.2,
                    "quantity": 12,
                },
            ],
        }
    ]

    result = create_objects_from_json(data)

    # Тип контейнера
    assert isinstance(result, list)
    assert len(result) == 1

    cat = result[0]

    # Проверяем интерфейс категории (duck-typing)
    assert hasattr(cat, "name")
    assert hasattr(cat, "description")
    assert hasattr(cat, "products")

    assert cat.name == "Fruits"
    assert cat.description == "Sweet and tasty"

    # Проверяем содержимое products в двух возможных вариантах реализации
    _assert_products_container(
        cat.products,
        [
            {"name": "Apple", "description": "Red", "price": 10.5, "quantity": 5},
            {"name": "Banana", "description": "Yellow", "price": 7.2, "quantity": 12},
        ],
    )


def test_create_objects_from_json_category_without_products():
    """Тест на категорию без продуктов (допускаем и пустой список, и пустую строку)."""
    data = [
        {"name": "EmptyCategory", "description": "No products here", "products": []}
    ]

    result = create_objects_from_json(data)
    assert isinstance(result, list)
    assert len(result) == 1

    cat = result[0]
    assert cat.name == "EmptyCategory"
    assert cat.description == "No products here"
    assert hasattr(cat, "products")

    # Нормируем поведение: либо пустой список, либо пустая/пробельная строка
    if isinstance(cat.products, list):
        assert cat.products == []
    elif isinstance(cat.products, str):
        assert cat.products.strip() == ""
    else:
        pytest.fail(f"Неожиданный тип products: {type(cat.products)!r}")
