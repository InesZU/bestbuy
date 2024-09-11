import pytest
from products import NonStockedProduct, LimitedProduct


def test_non_stocked_product():
    """Test that NonStockedProduct behaves correctly."""
    product = NonStockedProduct("Windows License", price=125)

    # Non-stocked products have an "infinite" quantity
    assert product.get_quantity() == float('inf')  # Should return infinite quantity
    assert product.is_active() is True  # Non-stocked products should always be active

    # Invalid purchase request should raise ValueError
    with pytest.raises(ValueError):
        product.buy(0)  # Can't buy 0 quantity, should raise ValueError

    # Valid purchase request should work and return the correct total price
    assert product.buy(1) == 125  # Buying 1 Windows License, should return correct price
    assert product.buy(5) == 125 * 5  # Buying 5 licenses should also work and return correct price


def test_limited_product():
    """Test that LimitedProduct behaves correctly."""
    product = LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
    assert product.get_quantity() == 250
    assert product.buy(1) == 10.0
    assert product.get_quantity() == 249

    with pytest.raises(ValueError):
        product.buy(2)  # Should not be allowed to purchase more than the limit


def test_limited_product_max_purchase():
    """Test that LimitedProduct enforces the maximum purchase limit correctly."""
    product = LimitedProduct("Shipping", price=10, quantity=250, maximum=3)
    total_price = product.buy(3)
    assert total_price == 30.0
    assert product.get_quantity() == 247

    with pytest.raises(ValueError):
        product.buy(4)  # Should raise an exception


def test_limited_product_invalid_quantity():
    """Test that LimitedProduct rejects invalid quantities."""
    product = LimitedProduct("Shipping", price=10, quantity=250, maximum=2)
    with pytest.raises(ValueError):
        product.buy(0)  # Quantity must be greater than zero
