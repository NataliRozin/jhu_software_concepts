import pytest # type: ignore
from src.order import Order # type: ignore
import re

# Fixture to create an order with two pizzas
@pytest.fixture
def sample_order():
    """
    Fixture to create an Order instance with two pizzas added.

    Returns:
        Order: An order containing two pizzas:
            - Pizza 1: thin crust, pesto sauce, mozzarella, mushrooms
            - Pizza 2: thick crust, marinara sauce, mozzarella, mushrooms
    """

    # Create a new Order instance
    order = Order()

    # Add first pizza
    order.input_pizza('thin', ['pesto'], 'mozzarella', ['mushrooms'])
    
    # Add second pizza
    order.input_pizza('thick', ['marinara'], 'mozzarella', ['mushrooms'])
    
    return order

@pytest.mark.order_mark
def test_order_initialization():
    # Create a new Order instance
    order = Order()

    # Assert that pizza objects are of type list
    assert isinstance(order.pizza_objects, list)

    # Assert that the pizza_objects list is empty
    assert order.pizza_objects == []

    # Assert that the initial cost is zero
    assert order.cost == 0

    # Assert that payment is not yet completed
    assert order.payment_done is False

@pytest.mark.order_mark
def test_order_str_output(sample_order):
    expected_output = (
        "Customer Requested:\n"
        "Crust: thin, Sauce: ['pesto'], Cheese: mozzarella, Toppings: ['mushrooms'], Cost: 11\n"
        "Crust: thick, Sauce: ['marinara'], Cheese: mozzarella, Toppings: ['mushrooms'], Cost: 11"
    )
    
    assert str(sample_order) == expected_output

# @pytest.mark.order
# def test_order_input(sample_order):
