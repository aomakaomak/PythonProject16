import pytest

from src.order import Order


def test_order_init(order1):
    assert order1.link == "link1"
    assert order1.price == 10
    assert order1.quantity == 1
    assert order1.amount == 10


def test_order_init_error():
    expected_message = "Количество должно быть >= 1"
    with pytest.raises(ValueError) as excinfo:
        Order("link2", 20, -1)
    assert str(excinfo.value) == expected_message


def test_add_order(order1, order2):
    order1.add_product()
    order2.add_product()
    assert Order.orders == [["link1", 1, 10], ["link2", 1, 20]]
