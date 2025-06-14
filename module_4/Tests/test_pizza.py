import pytest # type: ignore
from src.order import Order # type: ignore
from src.pizza import Pizza # type: ignore

@pytest.mark.parametrize(
    "crust, sauce, cheese, toppings, cost", [
        ('thin', ['pesto'], 'mozzarella', ['mushrooms'], 11),
        ('thick', ['marinara'], 'mozzarella', ['mushrooms'], 11),
        ('gluten free', ['marinara'], 'mozzarella', ['pineapple'], 11),
        ('thin', ['liv sauce', 'pesto'], 'mozzarella', ['mushrooms', 'pepperoni'], 18)
    ]
)

@pytest.mark.pizza_mark
def test_pizza_initialization(crust, sauce, cheese, toppings, cost):
    # Create a new Pizza instance with the current parameters
    pizza = Pizza(crust=crust, sauce=sauce, cheese=cheese, toppings=toppings)

    #--- CRUST ---#
    # Assert that crust is a string
    assert isinstance(pizza.crust, str)

    # Assert crust is 'thin'
    assert pizza.crust == crust

    #--- SUACE ---#
    # Assert that sauce is a list containing one variable - 'pesto'
    assert isinstance(pizza.sauce, list)
    
    # Assert all elements are strings
    assert all(isinstance(s, str) for s in pizza.sauce)

    # Assert sauce includes 'pesto'
    assert pizza.sauce == sauce

    #--- CHEESE ---#
    # Assert that cheese is a string
    assert isinstance(pizza.crust, str)

    # Assert that cheese is 'mozzarella'
    assert pizza.cheese == cheese

    #--- TOPPINGS ---#
    # Assert that toppings is a list
    assert isinstance(pizza.toppings, list)

    # Assert all elements are strings
    assert all(isinstance(t, str) for t in pizza.toppings)

    # Assert toppings include 'mushrooms'
    assert pizza.toppings == toppings

    #--- COST ---#
    # Assert cost is an integer
    assert isinstance(pizza._cost, int)
    
    # Assert cost is higher than 0
    assert pizza._cost > 0



@pytest.mark.parametrize(
    "crust, sauce, cheese, toppings, cost", [
        ('thin', ['pesto'], 'mozzarella', ['mushrooms'], 11),
        ('thick', ['marinara'], 'mozzarella', ['mushrooms'], 11),
        ('gluten free', ['marinara'], 'mozzarella', ['pineapple'], 11),
        ('thin', ['liv sauce', 'pesto'], 'mozzarella', ['mushrooms', 'pepperoni'], 18)
    ]
)

@pytest.mark.pizza_mark
def test_pizza_str(crust, sauce, cheese, toppings, cost):
    # Create a new Pizza instance with the current parameters
    pizza = Pizza(crust=crust, sauce=sauce, cheese=cheese, toppings=toppings)

    expected_output = f"Crust: {crust}, Sauce: {sauce}, Cheese: {cheese}, Toppings: {toppings}, Cost: {cost}"

    assert str(pizza) == expected_output