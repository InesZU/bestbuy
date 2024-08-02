class Product:
    def __init__(self, name: str, price: float, quantity: int):
        """Initializes a Product object with its name, price, and quantity.

        Args:
            name: The name of the product.
            price: The price of the product.
            quantity: The initial quantity of the product in stock.
        """
        if not name or price < 0 or quantity < 0:
            raise ValueError(
                "Invalid product details: Ensure name is non-empty, price is non-negative, and quantity is non-negative.")

        self.name=name
        self.active=True
        self.quantity=quantity
        self.price=price

    def get_quantity(self) -> int:
        """Returns the current quantity of the product."""
        return self.quantity

    def set_quantity(self, quantity: int):
        """Updates the product quantity and checks if it becomes zero.
        If so, it deactivates the product.

        Args:
            quantity: The new quantity for the product.
        """
        self.quantity=quantity
        if self.quantity <= 0:
            self.deactivate()

    def is_active(self) -> bool:
        """Checks if the product is active (available for purchase).

        Returns:
            True if the product is active, False otherwise.
        """
        return self.active

    def activate(self):
        """Sets the product to active (available for purchase)."""
        self.active=True

    def deactivate(self):
        """Sets the product to inactive (unavailable for purchase)."""
        self.active=False

    def show(self) -> str:
        """Returns a string representation of the product with name, price, and quantity."""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity: int) -> float:
        """Simulates buying a certain quantity of the product.

        Args:
            quantity: The quantity of the product to be purchased.

        Raises:
            ValueError: If the requested quantity is invalid (less than or equal to zero or exceeds available stock).

        Returns:
            The total price of the purchased items.
        """
        if quantity <= 0:
            raise ValueError("Quantity to buy should be greater than zero.")
        if quantity > self.quantity:
            raise ValueError("Not enough quantity available.")

        self.quantity-=quantity
        total_price=self.price * quantity
        if self.quantity == 0:
            self.deactivate()
        return total_price