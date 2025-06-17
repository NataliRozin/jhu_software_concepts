"""
This module contains unit tests for the order class.
"""

import pytest # type: ignore
from src.order import Order # type: ignore
from src.pizza import Pizza # type: ignore

# --- Fixtures ---

@pytest.fixture
def order_fixture():
    """Fixture to create a new Order instance for each test"""
    return Order()


# --- Test Cases ---

pizza_test_cases = [
    ('thin', ['pesto'], 'mozzarella', ['mushrooms'], 11),
    ('thick', ['marinara'], 'mozzarella', ['mushrooms'], 11),
    ('gluten free', ['marinara'], 'mozzarella', ['pineapple'], 11),
    ('thin', ['liv sauce', 'pesto'], 'mozzarella', ['mushrooms', 'pepperoni'], 18)
]


# ----- Test: Order Initialization -----

@pytest.mark.order
def test_order_initialization(order_fixture):
    """Checking that an order is initialized correctly"""
    order = order_fixture

    # Pizza objects should start as an empty list
    assert order.pizza_objects == [], "Pizza objects should be empty initially"

    # The cost should be zero when the order is first created
    assert order_fixture.total_cost == 0, "Initial cost should be zero"

    # The paid status should be False before any payment is made
    assert order_fixture.paid is False, "Order should not be marked as paid initially"


# ----- Test: __str__ Output -----

@pytest.mark.order
@pytest.mark.parametrize(
    "pizza_params_list",
    [
        [pizza_test_cases[0]],
        [pizza_test_cases[0], pizza_test_cases[1]],
        pizza_test_cases  # all pizzas
    ],
    ids=["one_pizza", "two_pizzas", "multiple_pizzas"]
)
def test_order_str_output(order_fixture, pizza_params_list):
    """
    Test the __str__ method of the Order class using real Pizza instances.

    This verifies that the string representation includes the correct
    number of pizzas and formats them properly, including manually set costs.
    """
    pizzas = []
    for crust, sauce, cheese, toppings, cost in pizza_params_list:
        pizza = Pizza(crust=crust, sauce=sauce, cheese=cheese, toppings=toppings)
        pizza.set_cost(cost)  # Manually assign cost for testing __str__
        pizzas.append(pizza)

    order_fixture.pizza_objects = pizzas

    expected_output = "Customer Requested:\n" + "\n".join(str(pizza) for pizza in pizzas)

    assert str(order_fixture) == expected_output


# ----- Test: input_pizza Method -----

@pytest.mark.order
@pytest.mark.parametrize("params", pizza_test_cases)
def test_order_input_with_mock(params, order_fixture):
    """Checking that input_pizza correctly adds a pizza and updates the total cost"""
    crust, sauce, cheese, toppings, cost = params

    order = order_fixture
    order.input_pizza(crust, sauce, cheese, toppings)

    # Ensure the pizza was added to the order
    assert len(order.pizza_objects) == 1, "One pizza should be added to the order"

    # Verify the total cost matches the pizza cost
    assert order.total_cost == cost, "Order cost should be the same as mocked pizza cost"


# ----- Test: order_paid Method -----

@pytest.mark.order
def test_order_paid(order_fixture):
    """Checking that the payment status changes when the order is paid"""
    # Call the method to mark the order as paid
    order_fixture.order_paid()

    # Check that the order is marked as paid
    assert order_fixture.paid is True
