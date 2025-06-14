import pytest # type: ignore
from src.order import Order # type: ignore
from src.pizza import Pizza # type: ignore

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
    order_1 = {'crust': 'thin', 'sauce': ['pesto'], 'cheese': 'mozzarella', 'toppings': ['mushrooms']}
    order_2 = {'crust': 'thick', 'sauce': ['marinara'], 'cheese': 'mozzarella', 'toppings': ['mushrooms']}
    
    return order_1, order_2

@pytest.mark.pizza_mark
def test_pizza_initialization(_, mock_pizza):
    # Create a new Pizza instance
    pizza = Pizza(
        crust='thin',
        sauce=['pesto'],
        cheese='mozzarella',
        toppings=['mushrooms']
    )

    # Assert that crust is 'thin'
    assert pizza.crust == 'thin'

    # Assert that sauce is a list containing one variable - 'pesto'
    assert isinstance(pizza.sauce, list)
    assert pizza.sauce == ['pesto']

    # Assert that cheese is 'mozarella'
    assert pizza.cheese == 'mozarella'

    # Assert that toppings is a list containing one variable - 'mushrooms'
    assert isinstance(pizza.toppings, list)
    assert pizza.toppings == ['mushrooms']
