class Pizza:
    #Pizza objects and associated cost
    def init (self, crust, sauce, cheese, toppings):
        '''This function initializes a pizza'''

        # Set pizza variables
        self.crust = {"thin": 5,
                      "thick": 6,
                      "GF": 8}
        self.sauce = {"marinara": 2,
                      "pesto": 3,
                      "liv sauce": 5}
        self.topping = {"pineapple": 1,
                        "pepperoni": 2,
                        "mushrooms": 3}
        self.cheese = "Mozarella"
        self.cost = 0

    def __str__(self):
        # Print a pizza
        # Print the cost of that pizza

    def cost (self):
        # Determine the cost of a pizza