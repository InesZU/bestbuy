from typing import List, Tuple
from products import Product


class Store:
    def __init__(self, product_list: List[Product]):
        """Initializes a Store object with a list of products."""
        self.products = product_list

    def add_product(self, product: Product):
        """Adds a product to the store's inventory."""
        self.products.append(product)

    def remove_product(self, product: Product):
        """Removes a product from the store's inventory."""
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Calculates and returns the total quantity of all active products."""
        total_quantity = sum(product.get_quantity() for product in self.products if product.is_active())
        return total_quantity

    def get_all_products(self) -> List[Product]:
        """Returns a list of all active products in the store."""
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        """Processes an order and returns the total price.

        Args:
            shopping_list: A list of tuples, where each tuple contains a product and its quantity.

        Returns:
            The total price of the order.
        """
        total_price = 0.0
        for requested_product, quantity in shopping_list:
            if not requested_product.is_active():
                print(f"Product {requested_product.name} is not available.")
                continue

            if quantity <= 0:
                print(f"Invalid quantity for {requested_product.name}.")
                continue

            try:
                total_price += requested_product.buy(quantity)
            except ValueError as e:
                print(f"Error with product {requested_product.name}: {e}")

        return total_price


if __name__ == "__main__":
    # Example product list for testing
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]

    # Initialize store
    store = Store(product_list)

    # Test get_all_products
    products = store.get_all_products()
    print(f"Total quantity of all products: {store.get_total_quantity()}")

    # Test order (buying 1 MacBook and 2 Bose Earbuds)
    print(f"Order total: €{store.order([(products[0], 1), (products[1], 2)]):.2f}")
