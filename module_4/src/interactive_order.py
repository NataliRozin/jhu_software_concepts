"""
This module handles the process of taking a pizza order from the user at a pizzeria.

The user is prompted to customize their pizza with choices for crust, sauce, and toppings.
They can also cancel the operation at any time by pressing 'Q'. The module ensures that only
valid inputs are accepted.

Functions:
- get_valid_input: Prompts the user for a list of valid options (e.g., sauces, toppings) and
  ensures all inputs are valid.
- choose_crust: Prompts the user to choose a pizza crust type from valid options:
  Thick, Thin, Gluten Free/GF.
- choose_sauce: Prompts the user to choose one or more sauces from valid options:
  Marinara, Pesto, Liv sauce.
- choose_toppings: Prompts the user to choose one or more toppings from valid options:
  Pineapple, Pepperoni, Mushrooms.
- take_order_from_user: Manages the full process of taking a pizza order, including multiple pizzas,
  and final confirmation of payment.

Cancellation: 
- The user can cancel the entire order process at any time by entering 'Q' at any prompt.

Payment:
- After finishing the order, the user is asked if they have paid. If confirmed, the order is marked
  as paid.

Example:
- The user is prompted to customize their pizza, adding crust, sauce, and toppings, and can continue
  to order more pizzas or cancel the order process.

"""

import sys
from .order import Order

def get_valid_input(prompt, valid_options, item_name):
    """
    Prompt the user to enter a list of valid items (e.g., sauces, toppings).

    This function repeatedly asks the user for input until a valid list of options
    from the predefined valid options is provided.

    :param str prompt: The message displayed to the user asking for input.
    :param list valid_options: A list of valid options that the user can choose from.
    :param str item_name: The name of the item being selected to personalize the prompt
                          and error messages.
    :return: A list of valid items chosen by the user, stripped of whitespace.
    :rtype: list of str

    :raises SystemExit: If the user enters 'q' to cancel the order.
    """

    while True:
        user_input = input(prompt).lower().strip()

        if user_input == 'q':
            print("Order canceled by user.")
            sys.exit(0)

        if not user_input:
            # User input is empty
            print(f"You must choose at least one {item_name}.")
            continue

        # Split input string into a list and remove any surrounding whitespace
        user_input_list = [obj.strip() for obj in user_input.split(",") if obj]

        # Check for any invalid entries
        invalid = [obj for obj in user_input_list if obj not in valid_options]
        if invalid:
            print(f"Invalid {item_name}(s): {', '.join(invalid)}. Allowed options are:"
                  f"{', '.join(valid_options)}.\n")
            continue

        return user_input_list

def choose_crust():
    """
    Ask the user to choose a pizza crust type.

    Valid options include Thick, Thin, Gluten Free (GF).

    :return: The chosen crust type(s).
    :rtype: list of str
    """
    prompt = "Choose a crust - Thick, Thin, Gluten Free (GF):\n"
    valid_options = ["thick", "thin", "gluten free", "gf"]

    return get_valid_input(prompt, valid_options, item_name="crust")

def choose_sauce():
    """
    Ask the user to choose one or more sauces for the pizza.

    Valid options include Marinara, Pesto, or Liv sauce.

    :return: The chosen sauce(s).
    :rtype: list of str
    """
    while True:
        # Promt user for sauce type(s)
        prompt = "Choose at least one sauce - Marinara, Pesto or Liv sauce:\n"
        valid_sauces = ["marinara", "pesto", "liv sauce"]

        return get_valid_input(prompt, valid_sauces, "sauce")

def choose_toppings():
    """
    Ask the user to choose one or more pizza toppings.

    Valid options include Pineapple, Pepperoni, Mushrooms.

    :return: The chosen topping(s).
    :rtype: list of str
    """
    while True:
        # Promt user for toppings
        prompt = "Choose at least one topping - Pineapple, Pepperoni, Mushrooms:\n"
        valid_toppings = ["pineapple", "pepperoni", "mushrooms"]

        return get_valid_input(prompt, valid_toppings, "topping")

def take_order_from_user():
    """
    Manage the process of taking a pizza order from the user.

    This includes allowing the user to order multiple pizzas with customizable crust,
    sauces, and toppings. The user can cancel the order at any time by pressing 'Q'.

    After the user finishes their order, the order is confirmed and marked as paid if
    the user has paid.

    :return: None
    """
    # Create a new Order instance to store pizzas
    order = Order()
    continue_ordering = True

    print("\n********************\n" +
          "Welcome to Neopolitan Pizza!\n" +
          "You're about to create your perfect pizza from scratch!\n" +
          "Take your time, customize your pizza just the way you like it.\n" +
          "And if you change your mind at any moment, just hit 'Q' to cancel.\n" +
          "********************\n\n"
          )

    # Loop to allow user to order multiple pizzas
    while continue_ordering:
        # Prompt user for pizza details: crust, sauce and toppings
        crust    = choose_crust()
        sauce    = choose_sauce()
        toppings = choose_toppings()

        # Add pizza to the order with given crust, sauces, default cheese (Mozzarella), and toppings
        order.input_pizza(crust, sauce, "Mozzarella", toppings)

        # Ask the user if they want to add another pizza
        another_pizza = input("Would you like to order another pizza? - Y/N\n")
        if another_pizza.lower() == 'n':
            continue_ordering = False

    # Ask if the user has paid for the order
    payment_confirmation = input("Have you paid for the order? - Y/N\n")
    if payment_confirmation.lower() == 'y':
        order.order_paid()  # Set the order to paid

    # Print final order summary
    print(order)
