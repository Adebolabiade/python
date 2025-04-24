inventory = {
    "mango" : {"quantity":50,  "price": 5},
    "apple" :{"quantity":80, "price": 7 },
    "eggplant" :{"quantity":90, "price": 8}
 }


def display_inventory(inventory):
    print("Inventory:")
    for item, details in inventory.items():
        print(f"{item.capitalize()} - Quantity: {details['quantity']}, Price: £{details['price']:.2f}")


display_inventory(inventory)



def sell_item(inventory, item_name, quantity_sold):
    if item_name in inventory:
        if inventory[item_name]["quantity"] >= quantity_sold:
            inventory[item_name]["quantity"] -= quantity_sold
            total_cost = quantity_sold * inventory[item_name]["price"]
            return f"Sold {quantity_sold} {item_name}(s) for £{total_cost:.2f}. Remaining stock: {inventory[item_name]['quantity']}"
        else:
            return f"Not enough {item_name} in stock. Available: {inventory[item_name]['quantity']}"
    else:
        return f"{item_name.capitalize()} not found in inventory."

# Test the sell_item function
print(sell_item(inventory, "mango", 10))
print(sell_item(inventory, "apple", 50))
print(sell_item(inventory, "eggplant", 5))