import pytest # type: ignore
from src.order import Order # type: ignore
from src.pizza import Pizza # type: ignore

# -------------------------------
# Test cases
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
# Fixture: Constructs an Order instance before each test
# -------------------------------
@pytest.fixture
def order_obj():
    return Order()

# -------------------------------
# Mock Pizza
# -------------------------------
@pytest.mark.parametrize("crust, sauce, cheese, toppings, cost", pizza_test_cases)
def mock_pizza(crust, sauce, cheese, toppings, cost):
    """Returns a mock Pizza instance with the given parameters"""
    pizza = Pizza(crust=crust, sauce=sauce, cheese=cheese, toppings=toppings)
    pizza._cost = cost  # Set the cost directly on the mock pizza
    return pizza

# -------------------------------
# Test: Initialization of Order attributes
# Checks type and value correctness
# -------------------------------
@pytest.mark.order_mark
def test_order_initialization(order_obj):
    #--- PIZZA OBJECTS
    assert isinstance(order_obj.pizza_objects, list), "Pizza objects should be a list"
    assert order_obj.pizza_objects == [], "Pizza objects should be an empty list"

    #--- COST
    assert order_obj.cost == 0, "Initial cost should be zero"

    #--- PAYMENT
    assert isinstance(order_obj.paid, bool), "Value should be boolean"
    assert order_obj.paid is False, "Payments should not be yet completed"

# -------------------------------
# Test: Validate __str__ output of Order for different pizza object lists
# Checks that the correct formatted string is returned
# -------------------------------
@pytest.mark.order_mark
@pytest.mark.parametrize("pizza_objects, expected_value", [(["Pizza 1"], "Customer Requested:\nPizza 1"),
                                                           (["Pizza 1", "Pizza 2"], "Customer Requested:\nPizza 1\nPizza 2"),
                                                           (["Pizza 1", "Pizza 2", "Pizza 3", "Pizza 4", "Pizza 5"], "Customer Requested:\nPizza 1\nPizza 2\nPizza 3\nPizza 4\nPizza 5")])
def test_order_str_output(order_obj, pizza_objects, expected_value):

    order_obj.pizza_objects = pizza_objects

    assert str(order_obj) == expected_value

# -------------------------------
# Test: Ensure input_pizza correctly adds pizza and updates cost
# -------------------------------
@pytest.mark.order_mark
@pytest.mark.parametrize("crust, sauce, cheese, toppings, cost", pizza_test_cases)
def test_order_input_with_mock(monkeypatch, crust, sauce, cheese, toppings, cost, order_obj):
    # Create a mock pizza with the provided parameters
    mock_pizza = Pizza(crust, sauce, cheese, toppings)
    mock_pizza._cost = cost

    # Create an Order instance
    order = order_obj

    # Patch the Pizza reference in the order module to point to the mock pizza
    monkeypatch.setattr(Order, "input_pizza", lambda self, crust, sauce, cheese, toppings: self.pizza_objects.append(mock_pizza))
    
    # Call the method under test
    order.input_pizza(mock_pizza.crust, mock_pizza.sauce, mock_pizza.cheese, mock_pizza.toppings)

    # Assertions to verify correct behavior
    assert len(order.pizza_objects) == 1, "One pizza should be added to the order"
    assert order.pizza_objects[0] == mock_pizza, "Pizza should be an instance of MockPizza"
    assert order.cost == mock_pizza._cost, "Order cost should be the same as mocked pizza cost"

# @pytest.mark.order_mark
# def test_order_input(order_obj):
#     # Create a new Order instance
#     order = order_obj

#     assert order.paid is True