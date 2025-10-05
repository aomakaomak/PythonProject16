# Product & Category Management

## 📌 Описание

Этот проект демонстрирует простую систему управления товарами и категориями на Python.  
Он включает:

- Класс `Product` — описание товара (имя, описание, цена, количество).
- Класс `Category` — описание категории с товарами, а также счётчики количества категорий и товаров.
- Утилиты для чтения JSON-файлов и преобразования их в объекты Python (`utils.py`).
- Набор автотестов на **pytest** (`test_products.py`, `test_categories.py`).

---

## 📂 Структура проекта

```
.
├── categories.py       # Модель Category
├── products.py         # Модель Product
├── utils.py            # Чтение JSON и преобразование в объекты
├── conftest.py         # Фикстуры pytest
├── test_categories.py  # Тесты для Category
├── test_products.py    # Тесты для Product
└── data/
    └── products.json   # Пример данных (ожидаемый вход)
```

---

## 🚀 Установка и запуск

### 1. Клонировать проект
```bash
git clone https://github.com/yourusername/product-category.git
cd product-category
```

### 2. Создать виртуальное окружение
```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```

### 3. Установить зависимости
```bash
pip install -r requirements.txt
```

> ⚠️ В проекте используются только стандартная библиотека Python и `pytest`.

---

## 🛠 Использование

### Пример с классами напрямую
```python
from products import Product
from categories import Category

# Создаём товары
product1 = Product("Cucumber", "Very tasty", 23.5, 10)
product2 = Product("Tomato", "Very fresh", 45.2, 20)

# Создаём категорию с товарами
vegetables = Category("Vegetables", "Fresh", [product1, product2])

print(vegetables.name)        # Vegetables
print(vegetables.description) # Fresh
print(len(vegetables.products))  # 2
```

### Пример с JSON
```python
from utils import read_file, create_objects_from_json

data = read_file("data/products.json")
categories = create_objects_from_json(data)

for category in categories:
    print(category.name, "-", category.description)
    for product in category.products:
        print("   •", product.name, product.price)
```

---

## ✅ Тестирование

В проекте есть unit-тесты на **pytest**:

```bash
pytest -v
```

Примеры проверок:
- Корректность инициализации `Product`.
- Корректность инициализации `Category` и глобальных счётчиков.

---

## 📊 Возможности для расширения

- Добавить методы в `Product` (например, изменение цены или остатка).
- Добавить методы в `Category` для фильтрации и поиска товаров.
- Реализовать сериализацию обратно в JSON.

---

В проекте также реализована новая функциональность:
2 дочерних класса от класса Product
проверка на сложение одинаковых классов
проверка на добавление в каетегорию только продукта и ничего более

## 📄 Лицензия

MIT License. Свободно для использования и модификации.
