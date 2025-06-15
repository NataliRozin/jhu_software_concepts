import pytest
import sys
from src.interactive_order import ( # type: ignore
    get_valid_input,
    choose_crust,
    choose_sauce,
    choose_toppings,
    take_order_from_user
)

# Fixture for patching input in tests
@pytest.fixture
def mock_input(monkeypatch):
    """Fixture to mock the `input` function for simulating user input."""
    def _mock_input(prompt, response):
        """
        Mock the built-in input function to return the provided response.
        
        Args:
        - prompt (str): The input prompt to simulate.
        - response (str): The simulated user response.
        """
        monkeypatch.setattr('builtins.input', lambda _: response)

    return _mock_input

# Simple mock Order class to replace the actual implementation
class MockOrder:
    """Mock class to simulate the behavior of the Order class."""

    def __init__(self):
        """
        Initialize the mock order with an empty list of pizzas and a paid status of False.
        """
        self.pizzas = []
        self.paid = False

    def input_pizza(self, crust, sauce, cheese, toppings):
        """
        Simulate adding a pizza to the order.

        Args:
        - crust (list): The crust type(s) chosen for the pizza.
        - sauce (list): The sauce type(s) chosen for the pizza.
        - cheese (str): The cheese type used in the pizza.
        - toppings (list): The toppings chosen for the pizza.
        """
        self.pizzas.append({
            'crust': crust,
            'sauce': sauce,
            'cheese': cheese,
            'toppings': toppings
        })

    def order_paid(self):
        """Simulate marking the order as paid."""
        self.paid = True

# Test for `get_valid_input`
def test_get_valid_input_valid_choice(mock_input):
    """Test that `get_valid_input` correctly accepts a valid user choice."""
    mock_input("Choose your topping:", "pepperoni")
    valid_choices = ["pineapple", "pepperoni", "mushrooms"]

    # Test with valid input
    result = get_valid_input("Choose your topping:", valid_choices, "topping")
    assert result == ["pepperoni"]

def test_get_valid_input_invalid_choice(mock_input):
    """Test that `get_valid_input` re-prompts for input if the user enters an invalid choice."""
    # Simulate invalid input and then valid input
    mock_input("Choose your topping:", "invalid_topping")
    mock_input("Choose your topping:", "pineapple")
    valid_choices = ["pineapple", "pepperoni", "mushrooms"]

    # Test with invalid input followed by valid input
    result = get_valid_input("Choose your topping:", valid_choices, "topping")
    assert result == ["pineapple"]

def test_get_valid_input_cancel(mock_input):
    """Test that `get_valid_input` correctly handles cancellation (user presses 'Q')."""
    with pytest.raises(OperationCanceledError):  # type: ignore # Expect the custom error to be raised
        mock_input("Choose your topping:", "q")

# Test for `choose_crust`
def test_choose_crust_valid(mock_input):
    """Test that `choose_crust` accepts a valid crust choice."""
    mock_input("Choose a crust - Thick, Thin, Gluten Free (GF):", "thin")

    # Test with valid input
    result = choose_crust()
    assert result == ["thin"]

def test_choose_crust_invalid(mock_input):
    """Test that `choose_crust` re-prompts the user for valid input after an invalid choice."""
    # Simulate invalid input followed by valid input
    mock_input("Choose a crust - Thick, Thin, Gluten Free (GF):", "invalid_crust")
    mock_input("Choose a crust - Thick, Thin, Gluten Free (GF):", "thick")

    result = choose_crust()
    assert result == ["thick"]

# Test for `choose_sauce`
def test_choose_sauce_valid(mock_input):
    """Test that `choose_sauce` accepts a valid sauce choice."""
    mock_input("Choose at least one sauce - Marinara, Pesto or Liv sauce:", "pesto")

    # Test with valid input
    result = choose_sauce()
    assert result == ["pesto"]

def test_choose_sauce_invalid(mock_input):
    """Test that `choose_sauce` re-prompts the user for valid input after an invalid choice."""
    # Simulate invalid input followed by valid input
    mock_input("Choose at least one sauce - Marinara, Pesto or Liv sauce:", "invalid_sauce")
    mock_input("Choose at least one sauce - Marinara, Pesto or Liv sauce:", "marinara")

    result = choose_sauce()
    assert result == ["marinara"]

# Test for `choose_toppings`
def test_choose_toppings_valid(mock_input):
    """Test that `choose_toppings` accepts valid topping choices."""
    mock_input("Choose at least one topping - Pineapple, Pepperoni, Mushrooms:", "mushrooms")

    # Test with valid input
    result = choose_toppings()
    assert result == ["mushrooms"]

def test_choose_toppings_invalid(mock_input):
    """Test that `choose_toppings` re-prompts the user for valid input after an invalid choice."""
    # Simulate invalid input followed by valid input
    mock_input("Choose at least one topping - Pineapple, Pepperoni, Mushrooms:", "invalid_topping")
    mock_input("Choose at least one topping - Pineapple, Pepperoni, Mushrooms:", "pepperoni")

    result = choose_toppings()
    assert result == ["pepperoni"]

# Test for `take_order_from_user` (integration test)
def test_take_order_from_user(mock_input, monkeypatch):
    """
    Integration test for `take_order_from_user` to ensure the full pizza ordering process
    works as expected, including order creation and payment confirmation.
    """
    # Mock the sequence of user inputs
    mock_input("Choose a crust - Thick, Thin, Gluten Free (GF):", "thin")
    mock_input("Choose at least one sauce - Marinara, Pesto or Liv sauce:", "pesto")
    mock_input("Choose at least one topping - Pineapple, Pepperoni, Mushrooms:", "pepperoni")
    mock_input("Would you like to order another pizza? - Y/N", "n")
    mock_input("Have you paid for the order? - Y/N", "y")

    # Create a MockOrder instance to simulate the order object
    order_mock = MockOrder()
    monkeypatch.setattr('src.interactive_order.Order', lambda: order_mock)

    # Run the function
    take_order_from_user()

    # Assert if the order was called correctly
    assert order_mock.pizzas == [{
        'crust': ["thin"],
        'sauce': ["pesto"],
        'cheese': "Mozzarella",
        'toppings': ["pepperoni"]
    }]
    assert order_mock.paid is True
