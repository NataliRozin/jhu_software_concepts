import pytest # type: ignore
from src.order import Order # type: ignore
from src.pizza import Pizza # type: ignore

### Fixture: Creates an Order instance before each test
@pytest.fixture
def order_obj():
    return Order()

### Test Cases
pizza_test_cases = [
    ('thin', ['pesto'], 'mozzarella', ['mushrooms'], 11),
    ('thick', ['marinara'], 'mozzarella', ['mushrooms'], 11),
    ('gluten free', ['marinara'], 'mozzarella', ['pineapple'], 11),
    ('thin', ['liv sauce', 'pesto'], 'mozzarella', ['mushrooms', 'pepperoni'], 18)
]

### Mock Pizza: Simulates a Pizza instance with the provided parameters
@pytest.fixture
def mock_pizza(crust, sauce, cheese, toppings, cost):
    """Creates a mock Pizza instance with the given parameters"""
    pizza = Pizza(crust=crust, sauce=sauce, cheese=cheese, toppings=toppings)
    pizza._cost = cost # Directly assign the cost to the mock pizza
    return pizza

### Checking order initialization
@pytest.mark.order_mark
def test_order_initialization(order_obj):
    # Pizza objects should start as an empty list
    assert isinstance(order_obj.pizza_objects, list), "Pizza objects should be a list"
    assert order_obj.pizza_objects == [], "Pizza objects should be empty initially"

    # The cost should be zero when the order is first created
    assert order_obj.cost == 0, "Initial cost should be zero"

    # The paid status should be False before any payment is made
    assert isinstance(order_obj.paid, bool), "Paid status should be a boolean"
    assert order_obj.paid is False, "Order should not be marked as paid initially"

### Checking that __str__ method returns the correct formatted string
@pytest.mark.order_mark
@pytest.mark.parametrize("pizza_objects, expected_value", [(["Pizza 1"], "Customer Requested:\nPizza 1"),
                                                           (["Pizza 1", "Pizza 2"], "Customer Requested:\nPizza 1\nPizza 2"),
                                                           (["Pizza 1", "Pizza 2", "Pizza 3", "Pizza 4", "Pizza 5"], "Customer Requested:\nPizza 1\nPizza 2\nPizza 3\nPizza 4\nPizza 5")])
def test_order_str_output(order_obj, pizza_objects, expected_value):

    order_obj.pizza_objects = pizza_objects
    
    # Check if the string representation of the order matches the expected value
    assert str(order_obj) == expected_value

### Checking that input_pizza correctly adds a pizza and updates the total cost
@pytest.mark.order_mark
@pytest.mark.parametrize("crust, sauce, cheese, toppings, cost", pizza_test_cases)
def test_order_input_with_mock(crust, sauce, cheese, toppings, cost, order_obj, mock_pizza):
    pizza = mock_pizza

    order_obj.input_pizza(crust, sauce, cheese, toppings)

    # Ensure the pizza was added to the order
    assert len(order_obj.pizza_objects) == 1, "One pizza should be added to the order"

    # Verify the total cost matches the pizza cost
    assert order_obj.cost == pizza._cost, "Order cost should be the same as mocked pizza cost"

### Checking that the payment status changes to True when the order is paid
@pytest.mark.order_mark
def test_order_paid(order_obj):
    # Call the method to mark the order as paid
    order_obj.order_paid()

    # Check that the order is marked as paid
    assert order_obj.paid is True