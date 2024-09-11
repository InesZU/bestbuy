from typing import Optional


class Product:
    def __init__(self, name: str, price: float, quantity: int, promotion: Optional['Promotion'] = None):
        """
        Initializes a Product with name, price, quantity, and promotion.

        Args:
            name (str): Product name.
            price (float): Product price.
            quantity (int): Product quantity.
            promotion (Optional[Promotion]): Optional promotion for the product.

        Raises:
            ValueError: If name is empty, price is negative, or quantity is negative.
        """
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid product details.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = quantity > 0
        self.promotion = promotion

    def get_quantity(self) -> int:
        """Returns the product quantity."""
        return self.quantity

    def set_quantity(self, quantity: int) -> None:
        """Sets product quantity and deactivates if zero or negative."""
        self.quantity = quantity
        if self.quantity <= 0:
            self.deactivate()

    def is_active(self) -> bool:
        """Returns whether the product is active."""
        return self.active

    def activate(self) -> None:
        """Activates the product."""
        self.active = True

    def deactivate(self) -> None:
        """Deactivates the product."""
        self.active = False

    def get_promotion(self) -> Optional['Promotion']:
        """Returns the applied promotion, if any."""
        return self.promotion

    def set_promotion(self, promotion: Optional['Promotion']) -> None:
        """Sets a promotion for the product."""
        self.promotion = promotion

    def show(self) -> str:
        """Returns a string representation of the product."""
        promotion_info = f"Promotion: {self.promotion}" \
            if self.promotion else "No promotion"
        return (f"{self.name}, Price: {self.price}, "
                f"Quantity: {self.quantity}, {promotion_info}")

    def buy(self, quantity: int) -> float:
        """
        Buys a specified quantity, applying the promotion if any.

        Args:
            quantity (int): Quantity to buy.

        Returns:
            float: Total price after promotion.

        Raises:
            ValueError: If quantity is invalid or exceeds stock.
        """
        if quantity <= 0:
            raise ValueError("Quantity to buy should be greater than zero.")
        if quantity > self.quantity:
            raise ValueError("Not enough quantity available.")

        # Apply promotion if any, otherwise calculate regular price
        total_price = self.promotion.apply_promotion(self, quantity) \
            if self.promotion else self.price * quantity

        # Decrement stock and deactivate if stock hits zero
        self.set_quantity(self.quantity - quantity)
        if self.quantity == 0:
            self.deactivate()

        return total_price


class NonStockedProduct(Product):
    """
    Represents a product with zero quantity that cannot be tracked.
    """

    def __init__(self, name: str, price: float):
        """
        Initializes a NonStockedProduct with name and price.
        """
        super().__init__(name, price, quantity=float('inf'))

    def set_quantity(self, quantity: int):
        """
        Overrides to prevent changing quantity.
        """
        pass

    def buy(self, quantity: int) -> float:
        """
        Buys a specified quantity of a non-stocked product.
        Always assumes unlimited stock.
        Args:
            quantity (int): Quantity to buy.
        Returns:
            float: Total price for the specified quantity.
        Raises:
            ValueError: If the quantity is less than or equal to zero.
        """
        if quantity <= 0:
            raise ValueError("Quantity to buy should be greater than zero.")

        total_price = self.promotion.apply_promotion(self, quantity) \
            if self.promotion else self.price * quantity

        return total_price

    def show(self) -> str:
        """Returns a string representation of the non-stocked product."""
        base_info = super().show()
        return f"{base_info}, Unlimited stock"


class LimitedProduct(Product):
    """
    Represents a product with a maximum purchase limit.
    """

    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        """
        Initializes a LimitedProduct with name, price, quantity, and max limit.

        Args:
            name (str): Product name.
            price (float): Product price.
            quantity (int): Product quantity.
            maximum (int): Max purchase limit.

        Raises:
            ValueError: If maximum is less than or equal to zero.
        """
        super().__init__(name, price, quantity)
        if maximum <= 0:
            raise ValueError("Maximum purchase limit must be greater than zero.")
        self.maximum = maximum

    def buy(self, quantity: int) -> float:
        """
        Buys a specified quantity, respecting the max limit.

        Args:
            quantity (int): Quantity to buy.

        Raises:
            ValueError: If quantity exceeds the maximum limit.
        """
        if quantity > self.maximum:
            raise ValueError("Cannot purchase more than the maximum allowed quantity.")
        return super().buy(quantity)

    def show(self) -> str:
        """Returns a string representation of the limited product."""
        base_info = super().show()
        return f"{base_info}, Max purchase limit: {self.maximum}"
