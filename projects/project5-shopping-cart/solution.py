# Project 5 — Mini Shopping Cart
# Author: your name here

menu = {
    1: ("Apple",  0.50),
    2: ("Banana", 0.30),
    3: ("Milk",   1.20),
    4: ("Bread",  2.00),
}

cart = {}   # { item_name: quantity }
total = 0.0

# display the menu
print("Menu:")
for key, (name, price) in menu.items():
    print(f"{key}. {name} - ${price:.2f}")
print("5. Checkout")

# shopping loop
while True:
    try:
        choice = int(input("Choose an item (1-5): "))

        if choice == 5:
            break

        if choice not in menu:
            print("Invalid choice, try again.")
            continue

        item_name, price = menu[choice]

        # ⭐ Bonus: ask quantity
        quantity = int(input(f"How many {item_name}s? "))

        # handle duplicate items
        if item_name in cart:
            cart[item_name] += quantity
        else:
            cart[item_name] = quantity

        total += price * quantity

        print(f"Added {quantity} x {item_name}")

    except ValueError:
        print("Please enter a valid number.")

# apply discount
if total > 5.0:
    discount = total * 0.10
    total -= discount
    print("10% discount applied!")

# print receipt
print("\n--- Receipt ---")
for item, qty in cart.items():
    print(f"{item} x{qty}")

print(f"Total: ${total:.2f}")
