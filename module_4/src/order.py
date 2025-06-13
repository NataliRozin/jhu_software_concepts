from .pizza import Pizza

class Order:
    def __init__ (self):
        '''This function initializes a customer order'''
        # An empty list to store pizza objects
        self.pizza_objects = []

        # Initialize order cost
        self.cost = 0

        # Flag to indicate if payment has been completed
        self.paid = False

    def __str__(self):
        # Print a customers complete order
        current_order = "Customer Requested:\n"
        
        for obj in self.pizza_objects:
            current_order += f"{obj}\n"

        return current_order.rstrip('\n')

    def input_pizza (self, crust, sauce, cheese, toppings):
        '''Add a pizza with specified options to the customer's order.'''

        # Create a new Pizza instance using the provided crust, sauce(s), cheese, and toppings
        pizza = Pizza(crust, sauce, cheese, toppings)

        # Add the newly created pizza object to the order's list of pizzas
        self.pizza_objects.append(pizza)
        
        # Update the total cost of the order by adding the cost of the new pizza
        self.cost = pizza.cost()

    def order_paid(self):
        # Set order as paid once payment has been collected
        self.paid = True