import pytest # type: ignore
from src.order import Order # type: ignore
from src.pizza import Pizza # type: ignore

@pytest.mark.pizza_mark
def test_pizza_initialization():
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

    # Assert that cheese is 'mozzarella'
    assert pizza.cheese == 'mozzarella'

    # Assert that toppings is a list containing one variable - 'mushrooms'
    assert isinstance(pizza.toppings, list)
    assert pizza.toppings == ['mushrooms']