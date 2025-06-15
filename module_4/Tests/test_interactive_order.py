"""
Unit tests for the interactive_order module.

This module tests user input-driven functions for pizza ordering,
including input validation and overall order flow.

Each test simulates user interaction using mocked input.
"""

import pytest  # type: ignore
from src.interactive_order import (  # type: ignore
    get_valid_input,
    choose_crust,
    choose_sauce,
    choose_toppings,
    take_order_from_user
)

# --- Fixtures and Mocks ---
@pytest.fixture
def mock_input(monkeypatch):
    """
    Fixture to mock the `input()` function for simulating user input.

    :param monkeypatch: pytest built-in fixture used to override built-in functions.
    :return: A function that can mock the input prompt with a predefined response.
    """
    def _mock_input(response):
        """
        Mock a single input prompt.

        :param response: The simulated user input to return.
        """
        monkeypatch.setattr('builtins.input', lambda _: response)

    return _mock_input


class MockOrder:
    """
    A mock version of the Order class to simulate order-related actions in tests.
    """

    def __init__(self):
        """
        Initialize the mock order with no pizzas and unpaid status.
        """
        self.pizzas = []
        self.paid = False

    def input_pizza(self, crust, sauce, cheese, toppings):
        """
        Simulate adding a pizza to the order.

        :param crust: List of crust type(s).
        :param sauce: List of sauce type(s).
        :param cheese: Cheese type string.
        :param toppings: List of topping(s).
        """
        self.pizzas.append({
            'crust': crust,
            'sauce': sauce,
            'cheese': cheese,
            'toppings': toppings
        })

    def order_paid(self):
        """
        Simulate the order being marked as paid.
        """
        self.paid = True


# --- Tests for get_valid_input ---
@pytest.mark.interactive_mark
def test_get_valid_input_valid_choice(mock_input_func):
    """
    Test that `get_valid_input()` returns a valid choice when entered.

    :param mock_input_func: Mocked input fixture to simulate user input.
    """
    mock_input_func("pepperoni")
    valid_choices = ["pineapple", "pepperoni", "mushrooms"]

    result = get_valid_input("Choose your topping:", valid_choices, "topping")
    assert result == ["pepperoni"], "Should return valid input in list form."


@pytest.mark.interactive_mark
def test_get_valid_input_invalid_choice(monkeypatch):
    """
    Test that `get_valid_input()` re-prompts after invalid input.

    Simulates two inputs: one invalid, then a valid one.
    """
    # First simulate invalid input, then overwrite input with valid
    responses = iter(["invalid_topping", "pineapple"])
    monkeypatch = pytest.MonkeyPatch()
    monkeypatch.setattr('builtins.input', lambda _: next(responses))

    valid_choices = ["pineapple", "pepperoni", "mushrooms"]

    result = get_valid_input("Choose your topping:", valid_choices, "topping")
    monkeypatch.undo()

    assert result == ["pineapple"], "Should re-prompt and accept valid second input."


@pytest.mark.interactive_mark
def test_get_valid_input_exit_on_q(monkeypatch):
    """
    Test that `get_valid_input()` calls `sys.exit(0)` when the user inputs 'q'.

    This simulates the user canceling the operation by entering 'q', which should
    cause the program to exit immediately with exit code 0.

    :param monkeypatch: pytest fixture to mock `input()` and simulate user input.
    :raises SystemExit: Expected when `sys.exit(0)` is called upon cancellation.
    """
    # Prepare input to simulate user typing 'q'
    monkeypatch.setattr('builtins.input', lambda _: 'q')

    # Expect SystemExit when user inputs 'q'
    with pytest.raises(SystemExit) as e:
        get_valid_input("Choose your topping:", ["pineapple", "pepperoni"], "topping")

    # Verify exit code (0 means normal exit)
    assert e.type == SystemExit
    assert e.value.code == 0


# --- Tests for choose_crust ---
@pytest.mark.interactive_mark
def test_choose_crust_valid(mock_input_func):
    """
    Test that `choose_crust()` accepts a valid crust input.

    :param mock_input_func: Mocked input fixture.
    """
    mock_input_func("thin")

    result = choose_crust()
    assert result == ["thin"], "Should accept valid crust type."


@pytest.mark.interactive_mark
def test_choose_crust_invalid(monkeypatch):
    """
    Test that `choose_crust()` re-prompts after an invalid input.

    :param monkeypatch: pytest fixture.
    """
    responses = iter(["invalid_crust", "thick"])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))

    result = choose_crust()
    assert result == ["thick"], "Should accept second valid crust input."


# --- Tests for choose_sauce ---
@pytest.mark.interactive_mark
def test_choose_sauce_valid(mock_input_func):
    """
    Test that `choose_sauce()` accepts a valid sauce input.

    :param mock_input_func: Mocked input fixture.
    """
    mock_input_func("pesto")

    result = choose_sauce()
    assert result == ["pesto"], "Should accept valid sauce input."


@pytest.mark.interactive_mark
def test_choose_sauce_invalid(monkeypatch):
    """
    Test that `choose_sauce()` re-prompts after an invalid input.

    :param monkeypatch: pytest fixture.
    """
    responses = iter(["invalid_sauce", "marinara"])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))

    result = choose_sauce()
    assert result == ["marinara"], "Should accept second valid sauce input."


# --- Tests for choose_toppings ---
@pytest.mark.interactive_mark
def test_choose_toppings_valid(mock_input_func):
    """
    Test that `choose_toppings()` accepts a valid toppings input.

    :param mock_input_func: Mocked input fixture.
    """
    mock_input_func("mushrooms")

    result = choose_toppings()
    assert result == ["mushrooms"], "Should accept valid toppings input."


@pytest.mark.interactive_mark
def test_choose_toppings_invalid(monkeypatch):
    """
    Test that `choose_toppings()` re-prompts after invalid input.

    :param monkeypatch: pytest fixture.
    """
    responses = iter(["invalid_topping", "pepperoni"])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))

    result = choose_toppings()
    assert result == ["pepperoni"], "Should accept second valid topping input."


# --- Integration Test for take_order_from_user ---
@pytest.mark.interactive_mark
def test_take_order_from_user(monkeypatch):
    """
    Integration test for `take_order_from_user()`.

    Simulates a complete order flow including crust, sauce, toppings selection,
    and payment. Verifies if the mocked Order object behaves as expected.

    :param monkeypatch: Pytest fixture to override actual Order class and input function.
    """
    responses = iter([
        "thin",          # crust
        "pesto",         # sauce
        "pepperoni",     # toppings
        "n",             # another pizza?
        "y"              # payment confirmation
    ])

    monkeypatch.setattr('builtins.input', lambda _: next(responses))

    order_mock = MockOrder()
    monkeypatch.setattr('src.interactive_order.Order', lambda: order_mock)

    take_order_from_user()

    assert order_mock.pizzas == [{
        'crust': ["thin"],
        'sauce': ["pesto"],
        'cheese': "Mozzarella",
        'toppings': ["pepperoni"]
    }], "Order should contain one correct pizza"

    assert order_mock.paid is True, "Order should be marked as paid"
