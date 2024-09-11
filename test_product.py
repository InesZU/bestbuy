import pytest
from products import Product


def test_create_normal_product():
    """Test that creating a product with valid details works."""
    product = Product("MacBook Air M2", price=1450, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 100
    assert product.is_active() is True


def test_create_product_with_invalid_details():
    """Test that creating a product with invalid details (empty name, negative price) raises a ValueError."""
    with pytest.raises(ValueError):
        Product("", price=1450, quantity=100)  # Empty name should raise ValueError
    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=-10, quantity=100)  # Negative price should raise ValueError
    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=1450, quantity=-5)  # Negative quantity should raise ValueError


def test_product_becomes_inactive_when_quantity_zero():
    """Test that when a product reaches 0 quantity, it becomes inactive."""
    product = Product("MacBook Air M2", price=1450, quantity=1)
    product.set_quantity(0)
    assert product.quantity == 0
    assert product.is_active() is False


def test_product_purchase_modifies_quantity_and_returns_price():
    """Test that buying a product modifies the quantity and returns the right total price."""
    product = Product("MacBook Air M2", price=1450, quantity=100)
    total_price = product.buy(2)  # Buying 2 items
    assert product.quantity == 98  # Quantity reduced by 2
    assert total_price == 1450 * 2  # Total price = price * quantity


def test_buying_larger_quantity_than_exists_raises_exception():
    """Test that buying more than the available stock raises a ValueError."""
    product = Product("MacBook Air M2", price=1450, quantity=10)
    with pytest.raises(ValueError):
        product.buy(20)  # Trying to buy more than available should raise ValueError
