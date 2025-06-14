from .order import Order

def get_valid_list_input(prompt, valid_options, item_name):
    while True:
        user_input = input(prompt).lower().strip()

        if not user_input:
            # User input is empty
            print(f"You must choose at least one {item_name}.")
            continue
        
        # Split input string into a list and remove any surrounding whitespace
        user_input_list = [obj.strip() for obj in user_input.split(",") if obj]

        # Check for any invalid entries
        invalid = [obj for obj in user_input_list if obj not in valid_options]
        if invalid:
            print(f"Invalid {item_name}(s): {', '.join(invalid)}. Allowed options are: {', '.join(valid_options)}.")
            continue
            
        return user_input_list

def choose_crust():
    while True:
        # Prompt user for crust type
        crust = input("Choose a crust - Thick, Thin, Gluten Free (GF):\n").lower().strip()
        
        # Validate input
        if crust not in ["thick", "thin", "gluten free", "gf"]:
            print("Invalid crust type. Please choose Thick, Thin, Gluten Free, or GF.")
        else:
            return crust

def choose_sauce():
    while True:
        # Promt user for sauce type(s)
        prompt = "Choose at least one sauce - Marinara, Pesto or Liv sauce:\n"
        valid_sauces = ["marinara", "pesto", "liv sauce"]

        return get_valid_list_input(prompt, valid_sauces, "sauce")

def choose_toppings():
    while True:
        # Promt user for toppings
        prompt = "Choose at least one topping - Pineapple, Pepperoni, Mushrooms:\n"
        valid_toppings = ["pineapple", "pepperoni", "mushrooms"]

        return get_valid_list_input(prompt, valid_toppings, "topping")

def take_order_from_user():
    # Create a new Order instance to store pizzas
    order = Order()
    continue_ordering = True

    # Loop to allow user to order multiple pizzas
    while continue_ordering:
        # Prompt user for pizza details: crust, sauce and toppings
        crust    = choose_crust()
        sauce    = choose_sauce()
        toppings = choose_toppings()
        
        # Add pizza to the order with given crust, sauces, default cheese (Mozzarella), and toppings
        order.input_pizza(crust, sauce, "Mozzarella", toppings)

        # Ask the user if they want to add another pizza
        another_pizza = input("Would you like to order another pizza? - Y/N\n")
        if another_pizza.lower() == 'n':
            continue_ordering = False
    
    # Print final order summary
    print(order)