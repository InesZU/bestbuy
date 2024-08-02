import store
import products

def display_products(store):
    """Displays all products in the store."""
    products_list = store.get_all_products()
    for i, product in enumerate(products_list):
        print(f"{i + 1}. {product.show()}")

def start(store):
    """
    Starts the store application and provides a user interface for interacting with it.

    Args:
        store: An instance of the Store class.
    """
    while True:
        print("\n   Store Menu")
        print("   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ")

        if choice == "1":
            display_products(store)

        elif choice == "2":
            total_quantity = store.get_total_quantity()
            print(f"\nTotal amount of items in store: {total_quantity}")

        elif choice == "3":
            shopping_list = []
            while True:
                display_products(store)

                try:
                    product_choice = int(input("\nWhich product # do you want? ")) - 1
                    quantity_choice = int(input("What amount do you want? "))
                except ValueError:
                    print("\nInvalid input. Please enter numbers only.")
                    continue

                products_list = store.get_all_products()
                if not (0 <= product_choice < len(products_list)):
                    print("\nInvalid product choice. Please try again.\n")
                    continue
                if quantity_choice <= 0:
                    print("\nQuantity must be valid. Please try again.\n")
                    continue

                selected_product = products_list[product_choice]
                shopping_list.append((selected_product, quantity_choice))

                another_product = input("Do you want to buy another product? (yes/no): \n").strip().lower()
                if another_product not in ('yes', 'y'):
                    break

            # Place the order and calculate total price
            total_price = store.order(shopping_list)
            print(f"\nTotal price of your order: €{total_price:.2f}\n")

        elif choice == '4':
            print("Thank you for visiting the shop, see you soon.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # setup initial stock of inventory
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250)
                    ]
    best_buy = store.Store(product_list)
    start(best_buy)