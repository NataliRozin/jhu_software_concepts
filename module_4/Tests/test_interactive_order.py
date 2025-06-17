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
        monkeypatch.setattr("builtins.input", lambda prompt=None: str(next(response_iter)))
    return _mock_input

# class MockOrder:
#     """
#     Mock class to simulate an Order object for testing the order flow.

#     :ivar pizzas: List to hold pizza dictionaries.
#     :type pizzas: list
#     :ivar paid: Flag indicating whether the order has been paid.
#     :type paid: bool
#     """

#     def __init__(self):
#         self.pizzas = []
#         self.paid = False

#     def input_pizza(self, crust, sauce, cheese, toppings):
#         """
#         Simulates adding a pizza to the order.

#         :param crust: Chosen crust type
#         :param sauce: Chosen sauce(s)
#         :param cheese: Cheese type(s)
#         :param toppings: List of toppings
#         """
#         self.pizzas.append({
#             'crust': crust,
#             'sauce': sauce,
#             'cheese': cheese,
#             'toppings': toppings
#         })

#     def get_cost(self):
#         """
#         Returns a fixed cost for the mock pizza order.
#         """
#         return 11

#     def order_paid(self):
#         """
#         Marks the order as paid.
#         """
#         self.paid = True


# --- Tests for get_valid_input ---

@pytest.mark.order
@pytest.mark.parametrize(
    "case",
    [
        {
            "user_input": ["", "abc", "pepperoni"],
            "valid_choices": ["pineapple", "pepperoni", "mushrooms"],
            "object": "topping",
            "expected_output": ["pepperoni"],
            "expect_exit": False,
        },
        {
            "user_input": ["pineapple, mushrooms, pineapple"],
            "valid_choices": ["pineapple", "pepperoni", "mushrooms"],
            "object": "topping",
            "expected_output": ["pineapple", "mushrooms"],
            "expect_exit": False,
        },
        {
            "user_input": ["", "abc", "thin, thick", "thin"],
            "valid_choices": ["thin", "thick", "gluten free"],
            "object": "crust",
            "expected_output": ["thin"],
            "expect_exit": False,
        },
        {
            "user_input": ["", "abc", "marinara,liv sauce"],
            "valid_choices": ["marinara", "pesto", "liv sauce"],
            "object": "sauce",
            "expected_output": ["marinara", "liv sauce"],
            "expect_exit": False,
        },
        {
            "user_input": ["q"],
            "valid_choices": ["pineapple", "pepperoni", "mushrooms"],
            "object": "topping",
            "expected_output": None,
            "expect_exit": True,
        },
    ],
    ids=["valid_single_topping", "duplicate_topping", "crust", "valid_multiple_sauces", "quit_input"],
)
def test_input(mock_input, case):
    """
    Test suite for get_valid_input function with various input scenarios.

    Checks:
    - Valid input returns expected list.
    - Multiple invalid inputs followed by a valid input.
    - Quit input 'q' raises SystemExit.

    :param monkeypatch: pytest monkeypatch fixture to override input
    """
    mock_input(case["user_input"])

    if case["expect_exit"]:
        with pytest.raises(SystemExit) as exc:
            get_valid_input("Choose:", case["valid_choices"], case["object"])
        assert exc.type == SystemExit and exc.value.code == 0
    else:
        result = get_valid_input("Choose:", case["valid_choices"], case["object"])
        assert result == case["expected_output"]


# --- Tests for choose_* helpers ---

@pytest.mark.order
@pytest.mark.parametrize(
    "func, inputs, expected",
    [
        (choose_crust, [" ", "thick"], "thick"),
        (choose_sauce, ["bad", "pesto"], ["pesto"]),
        (choose_toppings, ["fake", "mushrooms"], ["mushrooms"]),
        (choose_crust, ["q"], None)
    ],
    ids=["choose_crust", "choose_sauce", "choose_toppings", "choose_crust_exit"]
)
def test_choose_input_variants(mock_input, func, inputs, expected):
    mock_input(inputs)

    if expected is None:
        with pytest.raises(SystemExit):
            func()
    else:
        assert func() == expected

# --- take_order_from_user Integration Tests ---

@pytest.mark.order
@pytest.mark.parametrize(
    "responses_list, expect_exit, expected_exit_code",
    [
        # Valid single pizza, payment confirmed - normal exit
        (["thin", "pesto", "pepperoni", "n", "card", "y"], False, None),

        # Invalid payment method, then valid - normal exit
        (["thin", "pesto", "mushrooms", "n", "bitcoin", "cash", "y"], False, None),

        # Invalid confirmation, then valid payment confirmation - normal exit
        (["thin", "pesto", "mushrooms", "n", "cash", "maybe", "cash", "y"], False, None),

        # Multiple pizzas, declined first payment, then confirmed on second - normal exit
        ([
            "thin", "marinara", "pepperoni", "y",
            "gluten free", "pesto", "mushrooms", "n",
            "card", "n",   # First payment declined
            "card", "y"    # Second payment accepted
        ], False, None),

        # Cancel at payment method prompt - should exit
        (["thin", "pesto", "pepperoni", "n", "q"], True, 0),
    ],
)
def test_order_flow_all_variants(mock_input, responses_list, expect_exit, expected_exit_code):
    """
    Parameterized integration test for various pizza ordering flows through take_order_from_user.

    Mocks user inputs, simulates order process, and asserts the final payment status and pizza
    count.

    :param monkeypatch: pytest monkeypatch fixture to override input
    :param responses_list: list of input strings simulating user choices/prompts
    :param expected_paid: boolean, expected order payment status after completion
    :param expected_pizza_count: int, expected number of pizzas in the order
    """
    mock_input(responses_list)

    if expect_exit:
        with pytest.raises(SystemExit) as exc:
            take_order_from_user()
        assert exc.type == SystemExit
        assert exc.value.code == expected_exit_code
    else:
        # Just run the flow, expecting no SystemExit and normal completion
        take_order_from_user()
