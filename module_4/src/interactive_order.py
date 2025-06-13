from order import Order

def take_order_from_user():
    # Create a new Order instance to store pizzas
    order = Order()
    continue_ordering = True

    # Loop to allow user to order multiple pizzas
    while continue_ordering:
        # Prompt user for pizza detailsL crust, sauce and toppings
        crust    = input("Choose a crust - Thick, Thin, Gluten Free:\n").strip().lower()
        sauce    = input("Choose at least one sauce - Marinara, Pesto or Liv sauce:\n").strip().lower()
        toppings = input("Choose at least one topping - Pineapple, Pepperoni, Mushrooms:\n").strip().lower()
        
        # Split input strings into lists and remove any surrounding whitespace
        sauce_list    = [s.strip() for s in sauce.split(",") if s]
        toppings_list = [t.strip() for t in toppings.split(",") if t]

        # Add pizza to the order with given crust, sauces, default cheese (Mozzarella), and toppings
        order.input_pizza(crust, sauce_list, "Mozzarella", toppings_list)

        # Ask the user if they want to add another pizza
        another_pizza = input("Would you like to order another pizza? - Y/N\n")
        if another_pizza.lower() == 'n':
            continue_ordering = False
    
    # Print final order summary
    print(order)