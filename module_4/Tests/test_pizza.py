import pytest # type: ignore
from src.pizza import Pizza # type: ignore

# -------------------------------
# Shared test cases used across tests
# Each tuple represents: (crust, sauce, cheese, toppings, cost)
# -------------------------------
# Shared test data
pizza_test_cases = [
    ('thin', ['pesto'], 'mozzarella', ['mushrooms'], 11),
    ('thick', ['marinara'], 'mozzarella', ['mushrooms'], 11),
    ('gluten free', ['marinara'], 'mozzarella', ['pineapple'], 11),
    ('thin', ['liv sauce', 'pesto'], 'mozzarella', ['mushrooms', 'pepperoni'], 18)
]

# -------------------------------
# Fixture: Constructs a Pizza instance using the parameters from parametrize
# -------------------------------
@pytest.mark.parametrize("crust, sauce, cheese, toppings, cost", pizza_test_cases)
@pytest.fixture
def pizza_obj(crust, sauce, cheese, toppings):
    return Pizza(crust=crust, sauce=sauce, cheese=cheese, toppings=toppings)

# -------------------------------
# Test: Initialization of Pizza attributes
# Checks type, value correctness, and positive cost
# -------------------------------
@pytest.mark.pizza_mark
@pytest.mark.parametrize("crust, sauce, cheese, toppings, cost", pizza_test_cases)
def test_pizza_initialization(pizza_obj, crust, sauce, cheese, toppings, cost):
    pizza = pizza_obj

    # --- CRUST ---
    assert isinstance(pizza.crust, str), "Crust should be a string"
    assert pizza.crust == crust

    # --- SAUCE ---
    assert isinstance(pizza.sauce, list), "Sauce should be a list"
    assert all(isinstance(s, str) for s in pizza.sauce), "Each sauce should be a string"
    assert pizza.sauce == sauce

    # --- CHEESE ---
    assert isinstance(pizza.crust, str), "Cheese should be a string"
    assert pizza.cheese == 'mozzarella', "Cheese must be mozzarella"

    # --- TOPPINGS ---
    assert isinstance(pizza.toppings, list), "Toppings should be a list"
    assert all(isinstance(t, str) for t in pizza.toppings), "Each topping should be a string"
    assert pizza.toppings == toppings

    # --- COST ---
    assert isinstance(pizza._cost, int), "Cost should be an integer"
    assert pizza._cost > 0, "Cost should be higher than zero"

# -------------------------------
# Test: Validate __str__ output of Pizza for different pizza object lists
# Checks that the correct formatted string is returned
# -------------------------------
@pytest.mark.pizza_mark
@pytest.mark.parametrize("crust, sauce, cheese, toppings, cost", pizza_test_cases)
def test_pizza_str(pizza_obj, crust, sauce, cheese, toppings, cost):
    pizza = pizza_obj

    expected_output = f"Crust: {crust}, Sauce: {sauce}, Cheese: {cheese}, Toppings: {toppings}, Cost: {cost}"

    assert str(pizza) == expected_output

# -------------------------------
# Test: cost() method
# Checks that the correct computed value is returned
# -------------------------------
@pytest.mark.pizza_mark
@pytest.mark.parametrize("crust, sauce, cheese, toppings, cost", pizza_test_cases)
def test_pizza_cost(pizza_obj, cost):
    pizza = pizza_obj
    assert pizza.cost() == cost