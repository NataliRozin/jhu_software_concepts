from order import Order

def take_order_from_user():
    print("Welcome to the Python Pizza Shop!")
    
    crust    = input("Choose a crust - [Thick, Thin, Gluten Free]: ").strip().lower()
    sauce    = input("Choose at least one sauce - [Marinara, Pesto or Liv sauce]: ").strip().lower()
    toppings = input("Choose at least one topping - [Pineapple, Pepperoni, Mushrooms]: ").strip().lower()
    
    sauce_list    = [s.strip() for s in sauce.split(",") if s]
    toppings_list = [t.strip() for t in toppings.split(",") if t]

    order = Order()
    order.input_pizza(crust, sauce_list, toppings_list)