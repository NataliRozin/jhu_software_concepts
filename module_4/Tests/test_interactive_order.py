"""
This module contains unit tests for the interactive_order module.
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
    Fixture to patch the built-in input function with a sequence of predefined responses.

    :param monkeypatch: pytest's monkeypatch fixture to override builtins.input
    :return: Function that takes a list of responses and patches input accordingly
    """
    def _mock_input(responses):
        response_iter = iter(responses)
        monkeypatch.setattr("builtins.input", lambda _: next(response_iter))
    return _mock_input


class MockOrder:
    """
    Mock class to simulate an Order object for testing the order flow.

    Attributes:
        pizzas (list): List to hold pizza dictionaries.
        paid (bool): Flag indicating whether the order has been paid.
    """

    def __init__(self):
        self.pizzas = []
        self.paid = False

    def input_pizza(self, crust, sauce, cheese, toppings):
        """
        Simulates adding a pizza to the order.

        :param crust: Chosen crust type
        :param sauce: Chosen sauce(s)
        :param cheese: Cheese type(s)
        :param toppings: List of toppings
        """
        self.pizzas.append({
            'crust': crust,
            'sauce': sauce,
            'cheese': cheese,
            'toppings': toppings
        })

    def get_cost(self):
        """
        Returns a fixed cost for the mock pizza order.
        """
        return 11

    def order_paid(self):
        """
        Marks the order as paid.
        """
        self.paid = True


# --- Tests for get_valid_input ---

@pytest.mark.order_mark
def test_get_valid_input(monkeypatch):
    """
    Test suite for get_valid_input function with various input scenarios.

    Checks:
    - Valid input returns expected list.
    - Multiple invalid inputs followed by a valid input.
    - Quit input 'q' raises SystemExit.

    :param monkeypatch: pytest monkeypatch fixture to override input
    """
    valid = ["pineapple", "pepperoni", "mushrooms"]

    # Valid input immediately accepted
    monkeypatch.setattr("builtins.input", lambda _: "pepperoni")
    assert get_valid_input("Choose topping:", valid, "topping") == ["pepperoni"]

    # Invalid inputs followed by a valid one
    responses = iter(["", "invalid", "thin, thick", "thin"])
    monkeypatch.setattr("builtins.input", lambda _: next(responses))
    assert get_valid_input("Choose crust:", ["thin", "thick", "gluten free"], "crust") == ["thin"]

    # Input 'q' should raise SystemExit to quit gracefully
    monkeypatch.setattr("builtins.input", lambda _: "q")
    with pytest.raises(SystemExit) as e:
        get_valid_input("Choose topping:", valid, "topping")
    assert e.type == SystemExit and e.value.code == 0


# --- Tests for choose_* helpers ---

@pytest.mark.order_mark
def test_choose_input_variants(monkeypatch):
    """
    Tests for the input helper functions choose_crust, choose_sauce, and choose_toppings.

    Each helper is tested with invalid inputs first, then valid inputs, ensuring they
    properly re-prompt until a valid choice is made.

    :param monkeypatch: pytest monkeypatch fixture to override input
    """
    # choose_crust retries on blank input then accepts valid
    responses = iter([" ", "thick"])
    monkeypatch.setattr("builtins.input", lambda _: next(responses))
    assert choose_crust() == "thick"

    # choose_sauce retries on invalid then accepts valid, returns list
    responses = iter(["bad", "pesto"])
    monkeypatch.setattr("builtins.input", lambda _: next(responses))
    assert choose_sauce() == ["pesto"]

    # choose_toppings retries on invalid then accepts valid, returns list
    responses = iter(["fake", "mushrooms"])
    monkeypatch.setattr("builtins.input", lambda _: next(responses))
    assert choose_toppings() == ["mushrooms"]


# --- take_order_from_user Integration Tests ---

@pytest.mark.order_mark
@pytest.mark.parametrize(
    "responses_list, expected_paid, expected_pizza_count",
    [
        # Valid single pizza, payment confirmed
        (["thin", "pesto", "pepperoni", "n", "card", "y"], True, 1),

        # Invalid payment method, then valid
        (["thin", "pesto", "mushrooms", "n", "bitcoin", "cash", "y"], True, 1),

        # Invalid confirmation, then valid payment confirmation
        (["thin", "pesto", "mushrooms", "n", "cash", "maybe", "cash", "y"], True, 1),

        # Multiple pizzas, declined first payment, then confirmed on second
        ([
            "thin", "marinara", "pepperoni", "y",
            "gluten free", "pesto", "mushrooms", "n",
            "card", "n",   # First payment declined
            "card", "y"    # Second payment accepted
        ], True, 2),
    ]
)
def test_order_flow_variants(monkeypatch, responses_list, expected_paid, expected_pizza_count):
    """
    Parameterized integration test for various pizza ordering flows through take_order_from_user.

    Mocks user inputs, simulates order process, and asserts the final payment status and pizza
    count.

    :param monkeypatch: pytest monkeypatch fixture to override input
    :param responses_list: list of input strings simulating user choices/prompts
    :param expected_paid: boolean, expected order payment status after completion
    :param expected_pizza_count: int, expected number of pizzas in the order
    """
    responses = iter(responses_list)
    monkeypatch.setattr("builtins.input", lambda _: next(responses))

    order_mock = MockOrder()
    monkeypatch.setattr("src.interactive_order.Order", lambda: order_mock)

    try:
        take_order_from_user()
    except SystemExit:
        # Some flows may exit via sys.exit, which is expected in certain test scenarios
        pass

    assert order_mock.paid == expected_paid
    assert len(order_mock.pizzas) == expected_pizza_count


@pytest.mark.order_mark
def test_order_flow_quit_on_payment(monkeypatch):
    """
    Test immediate quit behavior when user enters 'q' during payment method selection.

    Verifies that take_order_from_user raises SystemExit and does not complete payment.

    :param monkeypatch: pytest monkeypatch fixture to override input
    """
    responses = iter(["thin", "pesto", "mushrooms", "n", "q"])
    monkeypatch.setattr("builtins.input", lambda _: next(responses))

    monkeypatch.setattr("src.interactive_order.Order", MockOrder)

    with pytest.raises(SystemExit) as e:
        take_order_from_user()

    assert e.type == SystemExit
    assert e.value.code == 0
