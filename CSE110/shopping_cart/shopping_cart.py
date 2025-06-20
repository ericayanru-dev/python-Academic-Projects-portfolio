"""
Author: Eric Ayanru
Course: CSE110
Project: Shopping Cart Program

Description:
This program allows users to manage a shopping cart. It supports:
- Adding items with price and quantity
- Viewing all items in the cart
- Removing an item
- Computing the total cost
- Exiting the program
"""

def display_menu():
    print("\nWelcome to the Shopping Cart Program!\n")
    print("Please select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")

def main():
    items = []
    prices = []
    quantities = []

    while True:
        display_menu()

        try:
            action = int(input("Please enter an action: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if action == 1:
            item = input("What item would you like to add? ").strip().title()
            try:
                price = float(input(f"What is the price of {item}? "))
                quantity = int(input(f"How many {item}s would you like to add? "))
            except ValueError:
                print("Invalid input for price or quantity.")
                continue

            items.append(item)
            prices.append(price)
            quantities.append(quantity)
            print(f"'{item}' has been added to the cart.")

        elif action == 2:
            if not items:
                print("Your cart is empty.")
            else:
                print("\nThe contents of the shopping cart are:")
                for i in range(len(items)):
                    print(f"{i + 1}. {items[i]} x{quantities[i]} @ ${prices[i]:.2f}")
                total = sum(prices[i] * quantities[i] for i in range(len(items)))
                print(f"Total price in cart: ${total:.2f}")

        elif action == 3:
            if not items:
                print("Your cart is empty.")
            else:
                try:
                    remove = int(input("Which item would you like to remove (number)? ")) - 1
                    if 0 <= remove < len(items):
                        print(f"Removing {items[remove]} from cart.")
                        items.pop(remove)
                        prices.pop(remove)
                        quantities.pop(remove)
                    else:
                        print("Invalid item number.")
                except ValueError:
                    print("Please enter a valid number.")

        elif action == 4:
            total = sum(prices[i] * quantities[i] for i in range(len(items)))
            print(f"The total price of the items in the shopping cart is: ${total:.2f}")

        elif action == 5:
            print("Thank you. Goodbye.")
            break

        else:
            print("Invalid selection. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
