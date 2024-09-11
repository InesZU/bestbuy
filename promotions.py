from abc import ABC, abstractmethod
from products import Product


class Promotion(ABC):
    """
    Abstract base class for promotions.
    Each promotion must implement the apply_promotion method.
    """
    def __init__(self, name: str):
        """Initializes the promotion with a name."""
        self.name = name

    @abstractmethod
    def apply_promotion(self, product: Product, quantity: int) -> float:
        """Apply the promotion and return the discounted total price."""
        pass

    def __str__(self) -> str:
        """Returns the name of the promotion."""
        return self.name


class PercentageDiscount(Promotion):
    """
    Applies a percentage discount to the total price of a product.
    """
    def __init__(self, name: str, percent: float):
        """
        Initializes a PercentageDiscount with a name and discount percentage.

        Args:
            name (str): The name of the discount promotion.
            percent (float): The percentage discount to apply.
        """
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product: Product, quantity: int) -> float:
        """
        Applies a percentage discount to the total price.

        Args:
            product (Product): The product to apply the promotion to.
            quantity (int): The quantity of the product.

        Returns:
            float: The total price after applying the percentage discount.

        Raises:
            ValueError: If quantity is not greater than zero.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        total_price = product.price * quantity
        discount = total_price * (self.percent / 100)
        return total_price - discount


class SecondItemHalfPrice(Promotion):
    """
    Applies a promotion where every second item is sold at half price.
    """
    def __init__(self, name: str):
        """
        Initializes a SecondItemHalfPrice promotion.

        Args:
            name (str): The name of the promotion.
        """
        super().__init__(name)

    def apply_promotion(self, product: Product, quantity: int) -> float:
        """
        Applies a second-item-half-price promotion to the total price.

        Args:
            product (Product): The product to apply the promotion to.
            quantity (int): The quantity of the product.

        Returns:
            float: The total price after applying the second-item-half-price promotion.

        Raises:
            ValueError: If quantity is not greater than zero.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if quantity < 2:
            return product.price * quantity

        half_price_items = quantity // 2
        full_price_items = quantity - half_price_items
        return (full_price_items * product.price) + (half_price_items * (product.price / 2))


class Buy2Get1Free(Promotion):
    """
    Applies a buy-2-get-1-free promotion to the total price.
    For every 2 items, 1 item is free.
    """
    def __init__(self, name: str):
        """
        Initializes a Buy2Get1Free promotion.

        Args:
            name (str): The name of the promotion.
        """
        super().__init__(name)

    def apply_promotion(self, product: Product, quantity: int) -> float:
        """
        Applies a buy-2-get-1-free promotion to the total price.
        For every 2 items, 1 item is free.

        Args:
            product (Product): The product to apply the promotion to.
            quantity (int): The quantity of the product.

        Returns:
            float: The total price after applying the buy-2-get-1-free promotion.

        Raises:
            ValueError: If quantity is not greater than zero.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        # Calculate the number of full-price items
        full_price_items = (2 * (quantity // 3)) + (quantity % 3)

        return full_price_items * product.price