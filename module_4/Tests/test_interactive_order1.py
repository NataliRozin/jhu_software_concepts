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
    def _mock_input(responses):
        response_iter = iter(responses)
        monkeypatch.setattr("builtins.input", lambda _: next(response_iter))
    return _mock_input


class MockOrder:
    def __init__(self):
        self.pizzas = []
        self.paid = False

    def input_pizza(self, crust, sauce, cheese, toppings):
        self.pizzas.append({
            'crust': crust,
            'sauce': sauce,
            'cheese': cheese,
            'toppings': toppings
        })

    def get_cost(self):
        return 11

    def order_paid(self):
        self.paid = True


# --- Tests for get_valid_input ---
@pytest.mark.int_mark
def test_get_valid_input(monkeypatch):
    valid = ["pineapple", "pepperoni", "mushrooms"]

    # Valid input
    monkeypatch.setattr("builtins.input", lambda _: "pepperoni")
    assert get_valid_input("Choose topping:", valid, "topping") == ["pepperoni"]

    # Invalids then valid
    responses = iter(["", "invalid", "thin, thick", "thin"])
    monkeypatch.setattr("builtins.input", lambda _: next(responses))
    assert get_valid_input("Choose crust:", ["thin", "thick", "gluten free"], "crust") == ["thin"]

    # Exit on 'q'
    monkeypatch.setattr("builtins.input", lambda _: "q")
    with pytest.raises(SystemExit) as e:
        get_valid_input("Choose topping:", valid, "topping")
    assert e.type == SystemExit and e.value.code == 0


# --- Tests for choose_* helpers ---
@pytest.mark.int_mark
def test_choose_input_variants(monkeypatch):
    # choose_crust
    responses = iter([" ", "thick"])
    monkeypatch.setattr("builtins.input", lambda _: next(responses))
    assert choose_crust() == "thick"

    # choose_sauce
    responses = iter(["bad", "pesto"])
    monkeypatch.setattr("builtins.input", lambda _: next(responses))
    assert choose_sauce() == ["pesto"]

    # choose_toppings
    responses = iter(["fake", "mushrooms"])
    monkeypatch.setattr("builtins.input", lambda _: next(responses))
    assert choose_toppings() == ["mushrooms"]


# --- take_order_from_user Integration Tests ---
@pytest.mark.int_mark
@pytest.mark.parametrize(
    "responses_list, expected_paid, expected_pizza_count",
    [
        # Valid single pizza, payment confirmed
        (["thin", "pesto", "pepperoni", "n", "card", "y"], True, 1),

        # Invalid payment method, then valid
        (["thin", "pesto", "mushrooms", "n", "bitcoin", "cash", "y"], True, 1),

        # Invalid confirmation, then valid
        (["thin", "pesto", "mushrooms", "n", "cash", "maybe", "cash", "y"], True, 1),

        # Multiple pizzas, declined payment, then confirmed
        (["thin", "marinara", "pepperoni", "y",
          "gluten free", "pesto", "mushrooms", "n", "card", "n", "card", "y"], True, 2),
    ]
)
def test_order_flow_variants(monkeypatch, responses_list, expected_paid, expected_pizza_count):
    """
    Parameterized test for multiple order flow scenarios using different simulated inputs.
    """
    responses = iter(responses_list)
    monkeypatch.setattr("builtins.input", lambda _: next(responses))

    order_mock = MockOrder()
    monkeypatch.setattr("src.interactive_order.Order", lambda: order_mock)

    try:
        take_order_from_user()
    except SystemExit:
        pass

    assert order_mock.paid == expected_paid
    assert len(order_mock.pizzas) == expected_pizza_count


# A test for immediate quit during payment method selection
@pytest.mark.int_mark
def test_order_flow_quit_on_payment(monkeypatch):
    responses = iter(["thin", "pesto", "mushrooms", "n", "q"])
    monkeypatch.setattr("builtins.input", lambda _: next(responses))

    monkeypatch.setattr("src.interactive_order.Order", lambda: MockOrder())

    with pytest.raises(SystemExit) as e:
        take_order_from_user()

    assert e.type == SystemExit
    assert e.value.code == 0
