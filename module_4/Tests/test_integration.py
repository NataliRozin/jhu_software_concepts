"""
Integration tests for the pizza ordering workflow in the interactive_order module.
"""

import pytest
import runpy
from src.interactive_order import take_order_from_user # type: ignore

@pytest.mark.order
def test_integration_order_flow(monkeypatch, capsys):
    """
    Integration test for the complete pizza ordering flow.

    This test simulates a user interacting with the pizza ordering system by providing
    inputs for two pizzas with different crusts, sauces, and toppings. It also tests
    the logic for ordering multiple pizzas and confirming payment.

    The test verifies:
    - The welcome message is printed.
    - The final printed order summary includes both pizzas with correct details.
    - The cost appears in the output.
    
    The user inputs simulated are:
    1. Crust for pizza 1: "thin"
    2. Sauces for pizza 1: "marinara,pesto"
    3. Toppings for pizza 1: "pineapple,pepperoni"
    4. Ordering another pizza? "y"
    5. Crust for pizza 2: "thick"
    6. Sauces for pizza 2: "liv sauce"
    7. Toppings for pizza 2: "mushrooms"
    8. Ordering another pizza? "n"
    9. Payment method: "cash" (added, as required by take_order_from_user)
    10. Payment confirmation: "y"

    :param monkeypatch: pytest fixture to patch built-in input function for simulating user input.
    :param capsys: pytest fixture to capture printed output during the test.
    """

    # Prepare simulated user inputs for the entire flow:
    inputs = iter([
        "thin",                  # choose crust pizza 1
        "marinara,pesto",        # choose sauces pizza 1
        "pineapple,pepperoni",   # choose toppings pizza 1
        "y",                     # order another pizza?
        "thick",                 # choose crust pizza 2
        "liv sauce",             # choose sauces pizza 2
        "mushrooms",             # choose toppings pizza 2
        "n",                     # no more pizzas
        "cash",                  # payment method
        "y"                      # payment confirmed
    ])

    # Patch input to return the next value from inputs each call
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Run the pizza ordering function
    runpy.run_path("main.py", run_name="__main__")

    # Capture printed output for assertions
    captured = capsys.readouterr()

    # Validate expected key outputs and pizza details in the printed output
    assert "Welcome to Neopolitan Pizza" in captured.out
    assert "Crust: thin" in captured.out
    assert "Sauce: ['marinara', 'pesto']" in captured.out
    assert "Toppings: ['pineapple', 'pepperoni']" in captured.out
    assert "Crust: thick" in captured.out
    assert "Sauce: ['liv sauce']" in captured.out
    assert "Toppings: ['mushrooms']" in captured.out
    assert "Your final cost is:" in captured.out
    assert "Thank you for your payment! Your order is complete." in captured.out
