import pytest
from PizzaOrder.order import Order

def test_order_initialization():
    order = Order()

    # Assert that the pizza_objects list is empty
    assert isinstance(order.pizza_objects, list)
    assert order.pizza_objects == []

    # Assert that the initial cost is zero
    assert order.cost == 0

    # Assert that payment is not yet completed
    assert order.payment_done is False