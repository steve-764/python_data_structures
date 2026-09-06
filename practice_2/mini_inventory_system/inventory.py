# create empty list for inventory
inventory = []

def add_product(inventory, name, price, quantity):
    product = {
               "name":name,
               "price":price,
               "quantity":quantity
               }
    inventory.append(product)

add_product(inventory, "Sugar 1kg", 150, 20)
add_product(inventory, "Rice 2kg", 320, 4)
add_product(inventory, "Milk 500ml", 60, 15)
add_product(inventory, "Bread", 70, 3)
add_product(inventory, "Cooking Oil 1L", 400, 8)


print(inventory)