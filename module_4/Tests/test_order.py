import pytest # type: ignore
from src.order import Order # type: ignore
from src.pizza import Pizza # type: ignore

### Fixture: Constructs an Order instance before each test
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

### Mock Pizza
@pytest.fixture
def mock_pizza(crust, sauce, cheese, toppings, cost):
    """Returns a mock Pizza instance with the given parameters"""
    pizza = Pizza(crust=crust, sauce=sauce, cheese=cheese, toppings=toppings)
    pizza._cost = cost  # Set the cost directly on the mock pizza
    return pizza

### Checking order initialization
@pytest.mark.order_mark
def test_order_initialization(order_obj):
    # Pizza objects
    assert isinstance(order_obj.pizza_objects, list), "Pizza objects should be a list"
    assert order_obj.pizza_objects == [], "Pizza objects should be an empty list"

    # Cost
    assert order_obj.cost == 0, "Initial cost should be zero"

    # Payment
    assert isinstance(order_obj.paid, bool), "Value should be boolean"
    assert order_obj.paid is False, "Payments should not be yet completed"

### Checking __str__ returns correct formatted string
@pytest.mark.order_mark
@pytest.mark.parametrize("pizza_objects, expected_value", [(["Pizza 1"], "Customer Requested:\nPizza 1"),
                                                           (["Pizza 1", "Pizza 2"], "Customer Requested:\nPizza 1\nPizza 2"),
                                                           (["Pizza 1", "Pizza 2", "Pizza 3", "Pizza 4", "Pizza 5"], "Customer Requested:\nPizza 1\nPizza 2\nPizza 3\nPizza 4\nPizza 5")])
def test_order_str_output(order_obj, pizza_objects, expected_value):

    order_obj.pizza_objects = pizza_objects

    assert str(order_obj) == expected_value

### Checking input_pizza correctly adds pizza and updates cost
@pytest.mark.order_mark
@pytest.mark.parametrize("crust, sauce, cheese, toppings, cost", pizza_test_cases)
def test_order_input_with_mock(crust, sauce, cheese, toppings, cost, order_obj, mock_pizza):
    pizza = mock_pizza

    order_obj.input_pizza(crust, sauce, cheese, toppings)

    # Assertions to verify correct behavior
    assert len(order_obj.pizza_objects) == 1, "One pizza should be added to the order"
    # assert order_obj.pizza_objects[0] == str(pizza), "Pizza should be an instance of MockPizza"
    assert order_obj.cost == pizza._cost, "Order cost should be the same as mocked pizza cost"

# @pytest.mark.order_mark
# def test_order_input(order_obj):
#     # Create a new Order instance
#     order = order_obj

#     assert order.paid is True