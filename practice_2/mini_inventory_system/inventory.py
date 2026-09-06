# create empty list for inventory
inventory = []

# adding a product to the inventory
def add_product(inventory, name, price, quantity):
    product = {
               "name":name,
               "price":price,
               "quantity":quantity
               }
    inventory.append(product)

# calculating total inventory cost

def total_value(inventory):
    total = 0
    for product in inventory:
        total += product["price"] * product["quantity"]

    return total

# finding low stock products, default 5 

def low_stock(inventory, threshold = 5):
    low_stock_products = []

    for product in inventory:
        if product["quantity"] < threshold:
            low_stock_products.append(product)

    return low_stock_products

# adding 5 products
add_product(inventory, "Sugar 1kg", 150, 20)
add_product(inventory, "Rice 2kg", 320, 4)
add_product(inventory, "Milk 500ml", 60, 15)
add_product(inventory, "Bread", 70, 3)
add_product(inventory, "Cooking Oil 1L", 400, 8)

# printing inventory
print("=" * 30)
print("         Current inventory")
for product in inventory:
    print(product)
print()
print("=" * 30)
print()

# printig  total inventory value
print(f"Total inventory value : {total_value(inventory)}")
print("=" * 30)
print()

# printing low stock products 
print("Low stock products")
print()
# using for loop to print each product on a new line
for product in low_stock(inventory):
    print(product)
print("=" * 30)
print()

# low stock with quantity < 10
print("Products stock with quantity < 10")
print()
for product in low_stock(inventory, 10):
    print(product)
print("=" * 30)

# finding the most expensive product

def most_expensive(inventory):
    highest_price = inventory[0]

    for product in inventory:
        if product["price"] > highest_price["price"]:
            highest_price = product

    return highest_price

print("=" * 30)
print()
print(f"MOst expensive product : {most_expensive(inventory)}")

# restocking a product

def restock(inventory, name, extra_qty):
    for product in inventory:
        if product["name"] == name:
            product["quantity"] += extra_qty
            return


restock(inventory, "Rice 2kg", 15)
restock(inventory, "Bread", 20)

print("=" * 30)
print("         Restocked inventory")
for product in inventory:
    print(product)
print()


# sort inventory by price
# using lambda function to get product prices as the key for the sorted function
#                                           par         expression
sorted_inv = sorted(inventory, key= lambda product: product["price"])

print("=" * 30)
print()
print("Sorted inventory by price:")

for product in sorted_inv:
    print(product)
