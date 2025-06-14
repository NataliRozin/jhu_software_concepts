class Pizza:
    #Pizza objects and associated cost
    def __init__ (self, crust, sauce, cheese, toppings):
        '''This function initializes a pizza'''

        # Set pizza variables
        self.crust    = crust
        self.sauce    = sauce
        self.cheese   = cheese
        self.toppings = toppings
        self._cost    = self.cost()
    
    def get_cost(self):
        return self._cost

    def __str__(self):
        # Print a pizza
        pizza_description = f"Crust: {self.crust}, Sauce: {self.sauce}, Cheese: {self.cheese}, Toppings: {self.toppings}, Cost: {self._cost}"

        return pizza_description

    def cost (self):
        # Menu prices
        crust_price    = {"thin": 5,
                          "thick": 6,
                          "gluten free": 8}
        
        sauce_price    = {"marinara": 2,
                          "pesto": 3,
                          "liv sauce": 5}
        
        toppings_price = {"pineapple": 1,
                          "pepperoni": 2,
                          "mushrooms": 3}
        
        # Determine the cost the chosen sauces and toppings
        sauce_cost    = sum(sauce_price[s.lower()] for s in self.sauce)
        toppings_cost = sum(toppings_price[t.lower()] for t in self.toppings)

        # Determine the cost of a pizza
        self._cost = sum([crust_price[self.crust.lower()], sauce_cost, toppings_cost])

        return self._cost