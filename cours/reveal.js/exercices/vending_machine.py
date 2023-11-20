import random

def create_profiles(client_names, starting_capital):
    return {name : starting_capital for name in client_names}

def create_vending_machine(products, prices):
    return {product : price for product, price in zip(products, prices)}

def buy_from_machine(client_profiles, vending_machine, client_name, product_name):
    """ write a function that creates a new client repository with modified
    capital after buying a specific item from the vending machine. """
    price = vending_machine[product_name]
    capital_client = client_profiles[client_name]
    new_capital_client = capital_client - price

    new_client_profiles = {}
    for name, capital in client_profiles.items():
        if name == client_name:
            new_client_profiles[name] = new_capital_client
        else:
            new_client_profiles[name] = capital
    
    new_client_profiles = {
        name : (new_capital_client if name == client_name else capital) 
        for name, capital 
        in client_profiles.items()
    }
    # ternaire: reponsePositive if condition else reponseNegative
    
    return new_client_profiles

def add_item_to_machine(vending_machine, item_name, price):
    new_vending_machine = {}
    for old_product, old_price in vending_machine.items():
        new_vending_machine[old_product] = old_price

    new_vending_machine[item_name] = price
    #=====================================================
    items = list(vending_machine.items())
    items.append((item_name, price))

    new_vending_machine = {
        product : cost
        for product, cost
        in items
    }

    return new_vending_machine

if __name__ == '__main__':

    client_names = ["Arnaud", "Monica", "Conrad", "Fabrice", "Sergey"]
    starting_capital = 5000
    client_profiles = create_profiles(client_names, starting_capital)
    print(client_profiles)

    products = ["Fanta", "Twix", "Mars", "Mentos", "Winston", "M&M's", "Panini"]
    prices = [random.randint(100, 1000) for _ in products] 

    vending_machine = create_vending_machine(products, prices)
    print(vending_machine)
    
    client_profiles = buy_from_machine(client_profiles, vending_machine, "Arnaud", "Twix")
    print(client_profiles)

    vending_machine = add_item_to_machine(vending_machine, "Evian", 200)
    print(vending_machine)
    