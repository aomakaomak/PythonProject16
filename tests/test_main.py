import pytest

@pytest.fixture
def product():
    return Developer('Ivan', 'Ivanov')