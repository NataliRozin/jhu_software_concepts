"""
order.py
========

This module contains the :class:`Order` class, which represents a customer order in a
pizza ordering system.

The :class:`Order` class allows:
    - adding pizzas to the order
    - calculating the total cost
    - marking the order as paid
"""

from src.pizza import Pizza # type: ignore

class Order:
    """
    This class represents a customer's pizza order.

    The `Order` class stores a list of pizzas, tracks the total cost, 
    and manages whether the order has been paid.
    """

    def __init__ (self):
        """
        Initialize a customer order, including an empty list of pizza objects, 
        the total cost of the order (set to 0), and a flag indicating that the 
        order has not been paid.
        
        :ivar list pizza_objects: A list to store pizza objects in the order.
        :ivar float cost: The total cost of the order, initially set to 0.
        :ivar bool paid: A flag indicating whether the order has been paid, initially False.
        """
        # An empty list to store pizza objects
        self.pizza_objects = []

        # Initialize order cost
        self.total_cost = 0

        # Flag to indicate if payment has been completed
        self.paid = False

    def __str__(self):
        """
        Generate a string representation of the customer's complete order, 
        listing the pizzas and their details.

        :return: A formatted string showing the pizzas in the order.
        :rtype: str
        """
        current_order = "Customer Requested:\n"

        # Concatenate all pizza orders into one string
        current_order += "\n".join(str(obj) for obj in self.pizza_objects)

        return current_order.rstrip('\n')

    def get_cost(self):
        """
        Get the total cost of the order.

        This method returns the cumulative cost of all pizzas currently
        added to the order. The cost is updated each time a pizza is added.

        :return: The total cost of the order.
        :rtype: float
        """
        return self.total_cost

    def input_pizza (self, crust, sauce, cheese, toppings):
        """
        Add a pizza with specified options to the customer's order.
        
        :param crust: The crust type of the pizza.
        :type crust: str
        :param sauce: The sauce(s) used on the pizza.
        :type sauce: str or list
        :param cheese: The cheese(s) used on the pizza.
        :type cheese: str or list
        :param toppings: The toppings added to the pizza.
        :type toppings: list

        :updates: 
            - pizza_objects (list): Adds the new pizza object to the list of pizzas in the order.
            - cost (float): Updates the total cost of the order by adding the cost of the new pizza.
        """

        # Create a new Pizza instance using the provided crust, sauce(s), cheese, and toppings
        pizza = Pizza(crust, sauce, cheese, toppings)

        # Add the newly created pizza object to the order's list of pizzas
        self.pizza_objects.append(pizza)

        # Update the total cost of the order by adding the cost of the new pizza
        self.total_cost += pizza.get_cost()

    def order_paid(self):
        """
        Mark the order as paid.

        :updates: 
            - paid (bool): Sets the 'paid' flag to True to indicate that order was paid.
        """
        # Set order as paid once payment has been collected
        self.paid = True
