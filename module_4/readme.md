# Name
Natali Rozin (JHED ID: nrozin1)

# Module Info
**Module 4:** Testing & Documentation

**Assignment:** Pytest and Sphinx

**Due Date:** 17/06/2025

---

# Approach

This assignment focuses on practicing **testing** and **documentation** skills by implementing a simulated pizza ordering system. The system allows users to interactively customize their pizzas by selecting a crust type, one or more sauces, and toppings. Users can order multiple pizzas in a single session, receive a detailed order summary, and complete the order through payment confirmation.

The pizza ordering system is designed as three main modules, each with a clear responsibility:

- **User Interface (`src/interactive_order.py`)**  
  Manages the interactive order-taking process.
  - Prompts users to select crust, sauces, and toppings with input validation and support for cancellation at any stage.
  - Allows ordering multiple pizzas within one session.  
  - Handles payment method selection and confirmation, enforcing payment before completing the order.
  - Ensures only valid inputs, removes duplicate sauces and toppings, and restricts crust selection to exactly one per pizza.

- **Order Management (`order.py`)**  
  Implements the `Order` class, responsible for managing the customer's order. 
  - Allows adding pizzas, calculating the total order cost, and marking the order as paid upon successful payment.
  - Provides a formatted summary string listing all pizzas in the order.

- **Pizza Representation (`pizza.py`)**  
  Implements the `Pizza` class, representing individual pizzas.
  - Stores attributes such as crust, sauces, cheese, and toppings.  
  - Calculates pizza cost based on predefined prices for crust, sauces, and toppings.  
  - Provides a string representation including detailed pizza information and cost.

Together, these modules model the pizza ordering workflow from user input through order creation and payment processing, with clear separation of concerns for maintainability and extensibility.

# Testing and Documentation

## Testing

- **Types of Tests:**
 This project includes both unit tests and integration tests to ensure comprehensive coverage.
 - *Unit tests* validate individual modules such as input validation, cost calculation, and order management.  
  - *Integration test* simulates a complete ordering session with multiple pizzas and payment confirmation, verifying the entire workflow and user interaction.

## Documentation 
  - Each module and function includes comprehensive docstrings following the **Sphinx** format.  
  - Clear descriptions of parameters, return values, and exceptions facilitate maintainability and ease onboarding for new developers.
  - Full documentation is available at:  
    [https://pizzaorder.readthedocs.io/en/latest/](https://pizzaorder.readthedocs.io/en/latest/)

This approach offers a hands-on example of applying core software engineering principles within a simple, real-world-inspired system

---

# How to Run
**Step 1:** Make sure you have **Python 3.0+** installed.

**Step 2:** Install the project dependencies by running:
```bash
pip install -r requirements.txt
```

## To interact with the pizza ordering system:
**Step 1:** Navigate to the project directory and execute:
```bash
python main.py
```

**Step 2:** Follow the on-screen prompts to customize your pizza order and complete the process.

## To run the tests:
Run the following command to execute tests marked with `order_mark` or `pizza_mark`:
```bash
pytest -v -m "order_mark or pizza_mark"
```