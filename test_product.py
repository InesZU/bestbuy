import pytest
from products import Product


def test_create_product():
    """Test that creating a normal product works."""
    product = Product("MacBook Air M2", price=1450, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.get_quantity() == 100
    assert product.is_active() is True


def test_create_product_with_invalid_details():
    """Test that creating a product with invalid details raises an exception."""
    with pytest.raises(ValueError):
        Product("", price=1450, quantity=100)  # Empty name
    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=-10, quantity=100)  # Negative price


def test_product_inactive_when_quantity_reaches_zero():
    """Test that when a product reaches 0 quantity, it becomes inactive."""
    product = Product("MacBook Air M2", price=1450, quantity=1)
    product.buy(1)  # Purchase all available quantity
    assert product.is_active() is False
    assert product.get_quantity() == 0


def test_product_purchase_modifies_quantity_and_returns_correct_output():
    """Test that product purchase modifies the quantity and returns the correct total price."""
    product = Product("MacBook Air M2", price=1450, quantity=100)
    total_price = product.buy(10)
    assert product.get_quantity() == 90
    assert total_price == 14500  # 10 * 1450


def test_buying_larger_quantity_than_exists_raises_exception():
    """Test that buying a larger quantity than exists raises an exception."""
    product = Product("MacBook Air M2", price=1450, quantity=5)
    with pytest.raises(ValueError):
        product.buy(10)  # Trying to buy more than available
