from .pizza import Pizza

class Order:
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
        # Print a customers complete order
        current_order = "Customer Requested:\n"

        # Concatenate all the pizza objects into one string
        "\n".join(str(obj) for obj in self.pizza_objects)

        return current_order.rstrip('\n')

    def input_pizza (self, crust, sauce, cheese, toppings):
        '''Add a pizza with specified options to the customer's order.'''

        # Create a new Pizza instance using the provided crust, sauce(s), cheese, and toppings
        pizza = Pizza(crust, sauce, cheese, toppings)

        # Add the newly created pizza object to the order's list of pizzas
        self.pizza_objects.append(pizza)

        # Update the total cost of the order by adding the cost of the new pizza
        self.cost += pizza.get_cost()

    def order_paid(self):
        # Set order as paid once payment has been collected
        self.paid = True
