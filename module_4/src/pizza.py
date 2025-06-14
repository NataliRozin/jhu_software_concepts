"""
pizza.py
This module defines a Pizza class, which represents a pizza with its attributes
(crust, sauce, cheese, toppings) and calculates its total cost based on selected options.
"""

class Pizza:
    """
    This class represents a pizza and calculates its cost based on selected crust, sauce, 
    cheese, and toppings.
    """

    def __init__ (self, crust, sauce, cheese, toppings):
        """
        Initialize a pizza with crust, sauce, cheese, and toppings.

        Parameters:
            crust (str):     Type of crust
            sauce (list):    List of sauces
            cheese (str):    Type of cheese
            toppings (list): List of toppings
            _cost (int):     The cost of the pizza
        """

        # Set pizza variables
        self.crust    = crust
        self.sauce    = sauce
        self.cheese   = cheese
        self.toppings = toppings
        self._cost    = self.cost()

    def get_cost(self):
        """
        Return the calculated cost of the pizza.
        """
        return self._cost

    def __str__(self):
        """
        Generate a string representation of the pizza, listing its details.

        Returns:
            str: A formatted string showing the pizza's crust, sauce, cheese, toppings, and cost.
        """

        pizza_description = (
            f"Crust: {self.crust}, "
            f"Sauce: {self.sauce}, "
            f"Cheese: {self.cheese}, "
            f"Toppings: {self.toppings}, "
            f"Cost: {self._cost}"
        )

        return pizza_description

    def cost (self):
        """
        Calculate the total cost of the pizza based on its crust, sauce, and toppings.
        
        Returns:
            int: The total cost of the pizza.
        """
        # Define the prices for each type of crust
        crust_price    = {"thin": 5,
                          "thick": 6,
                          "gluten free": 8}

        # Define the prices for each type of sauce
        sauce_price    = {"marinara": 2,
                          "pesto": 3,
                          "liv sauce": 5}

        # Define the prices for each topping
        toppings_price = {"pineapple": 1,
                          "pepperoni": 2,
                          "mushrooms": 3}

        # Calculate the cost the chosen sauces and toppings
        sauce_cost    = sum(sauce_price[s.lower()] for s in self.sauce)
        toppings_cost = sum(toppings_price[t.lower()] for t in self.toppings)

        # Calculate the cost of the pizza
        self._cost = sum([crust_price[self.crust.lower()], sauce_cost, toppings_cost])

        return self._cost
