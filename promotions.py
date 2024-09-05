from abc import ABC, abstractmethod
from products import Product


class Promotion(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product: Product, quantity: int) -> float:
        """Apply the promotion and return the discounted total price."""
        pass

    def __str__(self) -> str:
        return self.name


class PercentageDiscount(Promotion):
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

        full_price_items = quantity // 2
        half_price_items = quantity - full_price_items
        return (full_price_items * product.price) + (half_price_items * (product.price / 2))


class Buy2Get1Free(Promotion):
    def __init__(self, name: str):
        """
        Initializes a Buy2Get1Free promotion.

        Args:
            name (str): The name of the promotion.
        """
        super().__init__(name)

    class Buy2Get1Free(Promotion):
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

        # Calculate the number of items to be paid for
        paid_items = (quantity + 1) // 2

        return paid_items * product.price
