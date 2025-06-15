"""
This module contains unit tests for the pizza class.
"""

import pytest # type: ignore
from src.pizza import Pizza # type: ignore

# --- Test Cases ---
pizza_test_cases = [
    ('thin', ['pesto'], 'mozzarella', ['mushrooms'], 11),
    ('thick', ['marinara'], 'mozzarella', ['mushrooms'], 11),
    ('gluten free', ['marinara'], 'mozzarella', ['pineapple'], 11),
    ('thin', ['liv sauce', 'pesto'], 'mozzarella', ['mushrooms', 'pepperoni'], 18)
]

@pytest.mark.pizza_mark
@pytest.mark.parametrize("crust, sauce, cheese, toppings, _", pizza_test_cases)
def test_pizza_initialization(crust, sauce, cheese, toppings, _):
    """
    Test that a Pizza object is initialized with the correct attributes.

    :param crust: Crust type
    :param sauce: List of sauces
    :param cheese: Cheese type
    :param toppings: List of toppings
    :param _: Unused expected cost
    """
    pizza = Pizza(crust, sauce, cheese, toppings)

    # --- CRUST ---
    assert isinstance(pizza.crust, str), "Crust should be a string"
    assert pizza.crust == crust, "Crust does not match input"

    # --- SAUCE ---
    assert isinstance(pizza.sauce, list), "Sauce should be a list"
    assert all(isinstance(s, str) for s in pizza.sauce), "Each sauce should be a string"
    assert pizza.sauce == sauce, "Sauce list does not match input"

    # --- CHEESE ---
    assert isinstance(pizza.crust, str), "Cheese should be a string"
    assert pizza.cheese == 'mozzarella', "Cheese must be mozzarella"

    # --- TOPPINGS ---
    assert isinstance(pizza.toppings, list), "Toppings should be a list"
    assert all(isinstance(t, str) for t in pizza.toppings), "Each topping should be a string"
    assert pizza.toppings == toppings, "Toppings list does not match input"

    # --- COST ---
    assert isinstance(pizza.total_cost, int), "Cost should be an integer"
    assert pizza.total_cost > 0, "Cost should be higher than zero"

@pytest.mark.pizza_mark
@pytest.mark.parametrize("crust, sauce, cheese, toppings, expected_cost", pizza_test_cases)
def test_get_cost(crust, sauce, cheese, toppings, expected_cost):
    """
    Test that get_cost() returns the correct total cost of the pizza.

    :param crust: Crust type
    :param sauce: List of sauces
    :param cheese: Cheese type
    :param toppings: List of toppings
    :param expected_cost: Expected calculated cost
    """
    pizza = Pizza(crust, sauce, cheese, toppings)

    assert pizza.get_cost() == expected_cost, (
        f"Expected cost {expected_cost}, but got {pizza.get_cost()}"
    )

@pytest.mark.pizza_mark
@pytest.mark.parametrize("crust, sauce, cheese, toppings, cost", pizza_test_cases)
def test_set_cost(crust, sauce, cheese, toppings, cost):
    """
    Test that set_cost() correctly updates the total cost.

    :param crust: Crust type
    :param sauce: List of sauces
    :param cheese: Cheese type
    :param toppings: List of toppings
    :param cost: New cost to be set
    """
    pizza = Pizza(crust, sauce, cheese, toppings)
    pizza.set_cost(cost)

    assert pizza.total_cost == cost, (
        f"set_cost did not update total_cost correctly; expected {cost}, got {pizza.total_cost}"
    )

@pytest.mark.pizza_mark
@pytest.mark.parametrize("params", pizza_test_cases)
def test_pizza_str(params):
    """
    Test the __str__ method to verify string representation matches expectations.

    :param params: Tuple containing crust, sauce, cheese, toppings, and expected cost
    """
    crust, sauce, cheese, toppings, cost = params
    pizza = Pizza(crust, sauce, cheese, toppings)

    expected_output = (
                        f"Crust: {crust}, Sauce: {sauce}, Cheese: {cheese}, "
                        f"Toppings: {toppings}, Cost: {cost}"
                        )

    assert str(pizza) == expected_output, (
        f"String representation mismatch.\nExpected: {expected_output}\nGot: {str(pizza)}"
    )

@pytest.mark.pizza_mark
@pytest.mark.parametrize("crust, sauce, cheese, toppings, cost", pizza_test_cases)
def test_pizza_cost(crust, sauce, cheese, toppings, cost):
    """
    Test that the cost() method correctly computes the pizza's cost.

    :param crust: Crust type
    :param sauce: List of sauces
    :param cheese: Cheese type
    :param toppings: List of toppings
    :param cost: Expected computed cost
    """
    pizza = Pizza(crust, sauce, cheese, toppings)
    computed_cost = pizza.cost()

    assert computed_cost == cost, (
        f"Computed cost incorrect.\nExpected: {cost}\nGot: {computed_cost}"
    )
