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


def test_create_objects_from_json_valid():
    """Тест корректного преобразования JSON-данных"""
    data = [
        {
            "name": "Fruits",
            "description": "Sweet and tasty",
            "products": [
                {"name": "Apple", "description": "Red", "price": 10.5, "quantity": 5
                 },
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

    # Проверяем интерфейс и значения Category (без привязки к модулю класса)
    assert (
        hasattr(cat, "name")
        and hasattr(cat, "description")
        and hasattr(cat, "products")
    )
    assert cat.name == "Fruits"
    assert cat.description == "Sweet and tasty"
    assert isinstance(cat.products, list)
    assert len(cat.products) == 2

    # Проверяем интерфейс и значения Product
    p0, p1 = cat.products
    for p in (p0, p1):
        assert all(hasattr(p, a) for a in ("name", "description", "price", "quantity"))

    assert p0.name == "Apple"
    assert p0.description == "Red"
    assert p0.price == 10.5
    assert p0.quantity == 5

    assert p1.name == "Banana"
    assert p1.description == "Yellow"
    assert p1.price == 7.2
    assert p1.quantity == 12


def test_create_objects_from_json_empty_list():
    """Тест на пустой список категорий"""
    result = create_objects_from_json([])
    assert isinstance(result, list)
    assert result == []


def test_create_objects_from_json_category_without_products():
    """Тест на категорию без продуктов"""
    data = [
        {"name": "EmptyCategory", "description": "No products here", "products": []}
    ]

    result = create_objects_from_json(data)
    assert len(result) == 1
    cat = result[0]

    assert cat.name == "EmptyCategory"
    assert cat.description == "No products here"
    assert isinstance(cat.products, list)
    assert cat.products == []
