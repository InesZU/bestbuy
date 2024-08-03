from typing import Type


class Product:
    def __init__(self, name: str, price: float, quantity: int):
        """
        Initializes a Product with name, price, and quantity.

        Args:
            name (str): Product name.
            price (float): Product price.
            quantity (int): Product quantity.

        Raises:
            ValueError: If name is empty, price is negative, or quantity is negative.
        """
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid product details.")
        
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None

    def get_quantity(self) -> int:
        """
        Returns the product quantity.
        """
        return self.quantity

    def set_quantity(self, quantity: int):
        """
        Sets product quantity and deactivates if zero or negative.
        """
        self.quantity = quantity
        if self.quantity <= 0:
            self.deactivate()

    def is_active(self) -> bool:
        """
        Returns whether the product is active.
        """
        return self.active

    def activate(self):
        """
        Activates the product.
        """
        self.active = True

    def deactivate(self):
        """
        Deactivates the product.
        """
        self.active = False

    def get_promotion(self) -> 'Promotion':
        """
        Returns the applied promotion, if any.
        """
        return self.promotion

    def set_promotion(self, promotion: 'Promotion'):
        """
        Sets a promotion for the product.

        Args:
            promotion (Promotion): The promotion to apply to the product.
        """
        self.promotion = promotion

    def show(self) -> str:
        """
        Returns a string representation of the product.
        """
        promotion_info = f"Promotion: {self.promotion}" if self.promotion else "No promotion"
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, {promotion_info}"

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
        
        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = self.price * quantity

        self.quantity -= quantity
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
        super().__init__(name, price, 0)

    def set_quantity(self, quantity: int):
        """
        Overrides to prevent changing quantity.
        """
        pass


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
        """
        if quantity > self.maximum:
            raise ValueError("Cannot purchase more than the maximum allowed quantity.")
        return super().buy(quantity)
