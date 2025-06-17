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
    ids=["valid_single_topping", "duplicate_topping", "crust",
         "valid_multiple_sauces", "quit_input"],
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
    """
    Test the behavior of input-handling functions (choose_crust, choose_sauce, choose_toppings)
    with various user input scenarios.

    This test verifies that:
    - Invalid inputs are retried until valid inputs are received.
    - Valid inputs are returned correctly.
    - Entering 'q' causes the program to exit via SystemExit.

    :param mock_input: Fixture that mocks the built-in input() function.
    :type mock_input: Callable[[List[str]], None]
    :param func: The function being tested (choose_crust, choose_sauce, choose_toppings).
    :type func: Callable[[], str or List[str]]
    :param inputs: Simulated user inputs provided to the function.
    :type inputs: list[str]
    :param expected: Expected return value or None if SystemExit is expected.
    :type expected: str or list[str] or None
    """
    mock_input(inputs)

    if expected is None:
        with pytest.raises(SystemExit):
            func()
    else:
        assert func() == expected


# --- Functional Tests for Payment Flow in take_order_from_user ---

@pytest.mark.order
@pytest.mark.parametrize(
    "simulated_inputs, should_exit, expected_exit_code",
    [
        # Valid payment on first attempt
        (["thin", "pesto", "pepperoni", "n", "card", "y"], False, None),

        # Invalid payment method, then corrected
        (["thin", "pesto", "mushrooms", "n", "bitcoin", "cash", "y"], False, None),

        # Invalid payment confirmation, then valid
        (["thin", "pesto", "mushrooms", "n", "cash", "maybe", "cash", "y"], False, None),

        # Decline first payment, confirm on second attempt
        ([
            "thin", "marinara", "pepperoni", "y",
            "gluten free", "pesto", "mushrooms", "n",
            "card", "n", "card", "y"
        ], False, None),

        # User cancels at payment method prompt
        (["thin", "pesto", "pepperoni", "n", "q"], True, 0),
    ],
    ids=[
        "valid_first_payment",
        "correct_invalid_payment_method",
        "correct_invalid_confirmation",
        "second_attempt_successful_payment",
        "cancel_during_payment"
    ]
)
def test_payment_flow_scenarios(mock_input, simulated_inputs, should_exit, expected_exit_code):
    """
    Functional test for the payment interaction logic in `take_order_from_user`.

    Simulates various user behaviors related to the payment process:
    - Valid and invalid payment methods.
    - Confirmation retries.
    - Cancellation during payment selection.

    :param mock_input: Fixture to simulate built-in `input()` with predefined values.
    :param simulated_inputs: List of mocked user inputs during order and payment flow.
    :param should_exit: Whether SystemExit is expected (user cancels).
    :param expected_exit_code: Expected exit code if SystemExit is raised.
    """
    mock_input(simulated_inputs)

    if should_exit:
        with pytest.raises(SystemExit) as exc_info:
            take_order_from_user()
        assert exc_info.type == SystemExit
        assert exc_info.value.code == expected_exit_code
    else:
        take_order_from_user()
