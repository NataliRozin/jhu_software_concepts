"""
pizza.py
========

This module defines a Pizza class, which represents a pizza with its attributes
(crust, sauce, cheese, toppings) and calculates its total cost based on selected options.
"""

class Pizza:
    """
    Represents a pizza and calculates its cost based on selected crust, sauce, 
    cheese, and toppings.
    """

    crust_price = {
            "thin": 5,
            "thick": 6,
            "gluten free": 8
        }

    sauce_price = {
        "marinara": 2,
        "pesto": 3,
        "liv sauce": 5
    }

    toppings_price = {
        "pineapple": 1,
        "pepperoni": 2,
        "mushrooms": 3
    }

    def __init__(self, crust, sauce, cheese, toppings):
        """
        Initialize a pizza with crust, sauce, cheese, and toppings.

        :param crust: Type of crust (e.g., "thin", "thick", "gluten free")
        :type crust: str
        :param sauce: List of sauces (e.g., ["marinara", "pesto"])
        :type sauce: list[str]
        :param cheese: Type of cheese (e.g., "mozzarella")
        :type cheese: str
        :param toppings: List of toppings (e.g., ["mushrooms", "pepperoni"])
        :type toppings: list[str]
        """

        # Set attributes
        self.crust      = crust
        self.sauce      = sauce
        self.cheese     = cheese
        self.toppings   = toppings
        self.total_cost = self.cost()

    def get_cost(self):
        """
        Return the current cost of the pizza.

        :return: The pizza cost.
        :rtype: int
        """
        return self.total_cost

    def set_cost(self, cost):
        """
        Set the cost of the pizza explicitly.

        :param cost: The new cost to assign to the pizza.
        :type cost: int
        :raises ValueError: If the cost is not a non-negative integer.
        """
        if not isinstance(cost, int) or cost < 0:
            raise ValueError("Cost must be a non-negative integer.")
        self.total_cost = cost

    def __str__(self):
        """
        Return a string representation of the pizza.

        :return: A formatted string with pizza details.
        :rtype: str
        """
        pizza_description = (
            f"Crust: {self.crust}, "
            f"Sauce: {self.sauce}, "
            f"Cheese: {self.cheese}, "
            f"Toppings: {self.toppings}, "
            f"Cost: {self.total_cost}"
        )
        return pizza_description

    def cost(self):
        """
        Calculate the total cost of the pizza based on its crust, sauce, and toppings.

        :return: The calculated cost of the pizza.
        :rtype: int
        """
        # Get the base cost for the selected crust
        crust_cost    = Pizza.crust_price[self.crust.lower()]

        # Sum the cost of all selected sauces
        sauce_cost    = sum(Pizza.sauce_price[s.lower()] for s in self.sauce)

        # Sum the cost of all selected toppings
        toppings_cost = sum(Pizza.toppings_price[t.lower()] for t in self.toppings)

        # Total cost is the sum of crust, sauce, and topping costs
        final_cost = crust_cost + sauce_cost + toppings_cost

        return final_cost
