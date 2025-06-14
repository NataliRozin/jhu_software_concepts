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

    #--- CRUST ---#
    # Assert that crust is a string
    assert isinstance(pizza.crust, str)

    # Assert crust is 'thin'
    assert pizza.crust == 'thin'

    #--- SUACE ---#
    # Assert that sauce is a list containing one variable - 'pesto'
    assert isinstance(pizza.sauce, list)
    
    # Assert all elements are strings
    assert all(isinstance(s, str) for s in pizza.sauce)

    # Assert sauce includes 'pesto'
    assert pizza.sauce == ['pesto']

    #--- CHEESE ---#
    # Assert that cheese is a string
    assert isinstance(pizza.crust, str)

    # Assert that cheese is 'mozzarella'
    assert pizza.cheese == 'mozzarella'

    #--- TOPPINGS ---#
    # Assert that toppings is a list
    assert isinstance(pizza.toppings, list)

    # Assert all elements are strings
    assert all(isinstance(t, str) for t in pizza.toppings)

    # Assert toppings include 'mushrooms'
    assert pizza.toppings == ['mushrooms']

    #--- COST ---#
    # Assert cost is an integer
    assert isinstance(pizza._cost, int)
    
    # Assert cost is higher than 0
    assert pizza._cost > 0