from pizza import Pizza

class Order:
    def __init__ (self):
        '''This function initializes a customer order'''
        # An empty list to store pizza objects
        self.pizza_objects = []

        # Initialize order cost
        self.cost = 0

        # Flag to indicate if payment has been completed
        self.payment_done = False

    def __str__(self):
        # Print a customers complete order
        current_order = "Customer Requested:\n"
        
        for obj in self.pizza_objects:
            current_order += ""

        return current_order

    def input_pizza (self, crust, sauce, cheese, toppings):
        '''This function inputs the customers order for a given pizza'''

        # Initialize the pizza object
        pizza = Pizza(crust, sauce, cheese, toppings)

        # Attach to the order
        self.pizza_objects.append(pizza)
        for pizza in self.pizza_objects:
            print(pizza)
        
        # Update the cost
        a=1

    def order_paid(self):
        # Set order as paid once payment has been collected
        a=1