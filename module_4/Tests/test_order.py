"""
This module contains unit tests for the order class.
"""

import pytest # type: ignore
from src.order import Order # type: ignore
from src.pizza import Pizza # type: ignore

@pytest.fixture
def order_fixture():
    """Fixture to create a new Order instance for each test"""
    return Order()

### Test Cases
pizza_test_cases = [
    ('thin', ['pesto'], 'mozzarella', ['mushrooms'], 11),
    ('thick', ['marinara'], 'mozzarella', ['mushrooms'], 11),
    ('gluten free', ['marinara'], 'mozzarella', ['pineapple'], 11),
    ('thin', ['liv sauce', 'pesto'], 'mozzarella', ['mushrooms', 'pepperoni'], 18)
]

@pytest.fixture
def mock_pizza(crust, sauce, cheese, toppings, cost):
    """Creates a mock Pizza instance with the given parameters"""
    pizza = Pizza(crust=crust, sauce=sauce, cheese=cheese, toppings=toppings)
    pizza._cost = cost # Directly assign the cost to the mock pizza
    return pizza

@pytest.mark.order
def test_order_initialization(order_fixture):
    """Checking that an order is initialized correctly"""
    order = order_fixture

    # Pizza objects should start as an empty list
    assert order.pizza_objects == [], "Pizza objects should be empty initially"

    # The cost should be zero when the order is first created
    assert order_fixture.cost == 0, "Initial cost should be zero"

    # The paid status should be False before any payment is made
    assert order_fixture.paid is False, "Order should not be marked as paid initially"

### Checking that __str__ method returns the correct formatted string
@pytest.mark.order
@pytest.mark.parametrize("pizza_objects, expected_value",
                         [(["Pizza 1"], "Customer Requested:\nPizza 1"),
                          (["Pizza 1", "Pizza 2"], "Customer Requested:\nPizza 1\nPizza 2"),
                          (["Pizza 1", "Pizza 2", "Pizza 3", "Pizza 4", "Pizza 5"],
                           "Customer Requested:\nPizza 1\nPizza 2\nPizza 3\nPizza 4\nPizza 5"
                           )
                           ]
                           )
def test_order_str_output(order_fixture, pizza_objects, expected_value):
    """Checking that the string representation of the order is formatted correctly"""
    order = order_fixture

    order.pizza_objects = pizza_objects

    # Check if the string representation of the order matches the expected value
    assert str(order) == expected_value

### Checking that input_pizza correctly adds a pizza and updates the total cost
@pytest.mark.order
@pytest.mark.parametrize("crust, sauce, cheese, toppings, cost", pizza_test_cases)
def test_order_input_with_mock(crust, sauce, cheese, toppings, order_fixture, mock_pizza):
    """Checking that input_pizza correctly adds a pizza and updates the total cost"""
    order = order_fixture
    pizza = mock_pizza

    order.input_pizza(crust, sauce, cheese, toppings)

    # Ensure the pizza was added to the order
    assert len(order.pizza_objects) == 1, "One pizza should be added to the order"

    # Verify the total cost matches the pizza cost
    assert order.cost == pizza._cost, "Order cost should be the same as mocked pizza cost"

### Checking that the payment status changes to True when the order is paid
@pytest.mark.order
def test_order_paid(order_fixture):
    """Checking that the payment status changes when the order is paid"""
    order = order_fixture

    # Call the method to mark the order as paid
    order.order_paid()

    # Check that the order is marked as paid
    assert order.paid is True
