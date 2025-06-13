import pytest
from PizzaOrder.order import Order

@pytest.mark.order
def test_order_initialization():
    order = Order()

    # Assert that pizza objects are of type list
    assert isinstance(order.pizza_objects, list)

    # Assert that the pizza_objects list is empty
    assert order.pizza_objects == []

    # Assert that the initial cost is zero
    assert order.cost == 0

    # Assert that payment is not yet completed
    assert order.payment_done is False