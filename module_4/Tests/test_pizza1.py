"""
This module contains unit tests for the Pizza class.
"""

import pytest  # type: ignore
from src.pizza import Pizza  # type: ignore

# --- Test Cases ---
pizza_test_cases = [
    ('thin', ['pesto'], 'mozzarella', ['mushrooms'], 11),
    ('thick', ['marinara'], 'mozzarella', ['mushrooms'], 11),
    ('gluten free', ['marinara'], 'mozzarella', ['pineapple'], 11),
    ('thin', ['liv sauce', 'pesto'], 'mozzarella', ['mushrooms', 'pepperoni'], 18)
]

@pytest.fixture
def make_pizza():
    """
    Fixture that returns a Pizza object generator.
    """
    def _make_pizza(crust, sauce, cheese, toppings):
        return Pizza(crust, sauce, cheese, toppings)
    return _make_pizza


@pytest.mark.pizza_mark
@pytest.mark.parametrize("params", pizza_test_cases)
def test_pizza_initialization(make_pizza, params):
    """
    Verifies that a pizza is initialized correctly.
    """
    crust, sauce, cheese, toppings, expected_cost = params
    pizza = make_pizza(crust, sauce, cheese, toppings)

    # --- Crust ---
    assert isinstance(pizza.crust, str)
    assert pizza.crust == crust

    # --- Sauce ---
    assert isinstance(pizza.sauce, list)
    assert all(isinstance(s, str) for s in pizza.sauce)
    assert pizza.sauce == sauce

    # --- Cheese ---
    assert isinstance(pizza.cheese, str)
    assert pizza.cheese == 'mozzarella'

    # --- Toppings ---
    assert isinstance(pizza.toppings, list)
    assert all(isinstance(t, str) for t in pizza.toppings)
    assert pizza.toppings == toppings

    # --- Cost ---
    assert isinstance(pizza.get_cost(), int)
    assert pizza.get_cost() == expected_cost


@pytest.mark.pizza_mark
@pytest.mark.parametrize("params", pizza_test_cases)
def test_pizza_get_cost(make_pizza, params):
    """
    Verifies that get_cost() returns the correct cost.
    """
    crust, sauce, cheese, toppings, cost = params
    pizza = make_pizza(crust, sauce, cheese, toppings)

    assert pizza.get_cost() == cost


@pytest.mark.pizza_mark
@pytest.mark.parametrize("params", pizza_test_cases)
def test_pizza_str(make_pizza, params):
    """
    Verifies the string representation of the Pizza object.
    """
    crust, sauce, cheese, toppings, cost = params
    pizza = make_pizza(crust, sauce, cheese, toppings)

    expected_output = (
        f"Crust: {crust}, Sauce: {sauce}, Cheese: {cheese}, "
        f"Toppings: {toppings}, Cost: {cost}"
    )
    assert str(pizza) == expected_output


@pytest.mark.pizza_mark
@pytest.mark.parametrize("params", pizza_test_cases)
def test_pizza_cost(make_pizza, params):
    """
    Verifies that cost() method returns the correct computed value.
    """
    crust, sauce, cheese, toppings, cost = params
    pizza = make_pizza(crust, sauce, cheese, toppings)

    assert pizza.cost() == cost
