"""
order.py
This module contains the 'Order' class, which represents a customer order in a
pizza ordering system.

The 'Order' class allows adding pizzas to the order, calculating the total cost, 
and marking the order as paid.
"""

from src.pizza import Pizza # type: ignore

class Order:
    """
    This class represents a customer's pizza order.

    The 'Order' class stores a list of pizzas, tracks the total cost, 
    and manages whether the order has been paid.
    """

    def __init__ (self):
        """
        Initialize a customer order, including an empty list of pizza objects, 
        the total cost of the order (set to 0), and a flag indicating that the 
        order has not been paid.

        Attributes:
            pizza_objects (list): A list to store pizza objects in the order.
            cost (float): The total cost of the order, initially set to 0.
            paid (bool): A flag indicating whether the order has been paid, initially False.
        """
        # An empty list to store pizza objects
        self.pizza_objects = []

        # Initialize order cost
        self.cost = 0

        # Flag to indicate if payment has been completed
        self.paid = False

    def __str__(self):
        """
        Generate a string representation of the customer's complete order, 
        listing the pizzas and their details.

        Returns:
            str: A formatted string showing the pizzas in the order.
        """
        current_order = "Customer Requested:\n"

        # Concatenate all pizza orders into one string
        current_order += "\n".join(str(obj) for obj in self.pizza_objects)

        return current_order.rstrip('\n')

    def input_pizza (self, crust, sauce, cheese, toppings):
        """
        Add a pizza with specified options to the customer's order.

        Updates:
            pizza_objects (list): Adds the new pizza object to the list of pizzas in the order.
            cost (float): Updates the total cost of the order by adding the cost of the new pizza.
        
        """

        # Create a new Pizza instance using the provided crust, sauce(s), cheese, and toppings
        pizza = Pizza(crust, sauce, cheese, toppings)

        # Add the newly created pizza object to the order's list of pizzas
        self.pizza_objects.append(pizza)

        # Update the total cost of the order by adding the cost of the new pizza
        self.cost += pizza.get_cost()

    def order_paid(self):
        """
        Mark the order as paid.

        Updates:
            paid (bool): Sets the 'paid' flag to True to indicate that order was paid.
        """
        # Set order as paid once payment has been collected
        self.paid = True
