# Mini Inventory System for a Shop

Build a small inventory system for a shop. Each product is stored as a dictionary with three keys — name, price, and quantity — and all products live together in one list. You'll write three separate functions instead of one long script.

## What your program needs to do

1. Represent one product as a dictionary: `{"name": "Sugar 1kg", "price": 150, "quantity": 20}`.
2. Represent the whole shop as a list of these dictionaries, e.g. `inventory = []`.
3. Write `add_product(inventory, name, price, qty)` — it builds a dictionary from the four arguments and appends it to the inventory list. It should not return anything; it just modifies the list in place.
4. Write `total_value(inventory)` — it loops through every product, adds up price × quantity for each one, and returns the grand total.
5. Write `low_stock(inventory, threshold=5)` — it loops through the products and returns a new list containing only the products whose quantity is below the threshold. Note the default value of 5, so the function can be called as `low_stock(inventory)` or `low_stock(inventory, 10)`.
6. Add at least 5 different products using `add_product()`, then call and print the results of `total_value()` and `low_stock()`.

## Example test data

\`\`\`python
add_product(inventory, "Sugar 1kg", 150, 20)
add_product(inventory, "Rice 2kg", 320, 4)
add_product(inventory, "Milk 500ml", 60, 15)
add_product(inventory, "Bread", 70, 3)
add_product(inventory, "Cooking Oil 1L", 400, 8)

print(total_value(inventory))     # sum of price * quantity for all 5
print(low_stock(inventory))       # products with quantity < 5
print(low_stock(inventory, 10))   # products with quantity < 10
\`\`\`

## Stretch goal (optional, still in scope)

These reuse the same list-of-dicts idea, so they're a natural next step:

- `most_expensive(inventory)` — returns the single product dict with the highest price.
- `restock(inventory, name, extra_qty)` — finds a product by name and increases its quantity.
- Sort the inventory by price before printing it, using `sorted()` with a key function.