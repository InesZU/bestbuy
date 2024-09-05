import pytest
from products import Product, NonStockedProduct, LimitedProduct
from promotions import PercentageDiscount, SecondItemHalfPrice, Buy2Get1Free


# Create a setup fixture to initialize common test data
@pytest.fixture
def setup_products():
    # Setup initial stock of inventory
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
        NonStockedProduct("Windows License", price=125),
        LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
    ]

    # Create promotion catalog
    second_half_price = SecondItemHalfPrice("Second item at half price")
    third_one_free = Buy2Get1Free("Buy 2, get 1 free")
    thirty_percent = PercentageDiscount("30% off", percent=30)

    # Add promotions to products
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)

    return product_list


def test_percentage_discount(setup_products):
    product = next(p for p in setup_products if p.name == "Windows License")
    assert product.buy(1) == 87.5  # 125 - 30% = 87.5
    assert product.buy(2) == 175.0  # 125 * 2 - 30% of 250 = 175


def test_second_item_half_price(setup_products):
    product = next(p for p in setup_products if p.name == "MacBook Air M2")
    assert product.buy(1) == 1450
    assert product.buy(2) == 2175  # 1450 + (1450 / 2) = 2175


def test_buy2_get1_free(setup_products):
    product = next(p for p in setup_products if p.name == "Bose QuietComfort Earbuds")
    # Verify the correct price calculation with the promotion applied
    assert product.buy(2) == 250  # Buy 2, get 1 free, so you pay for 1
    assert product.buy(3) == 500  # Buy 3, get 1 free, pay for 2


def test_limited_product(setup_products):
    product = next(p for p in setup_products if p.name == "Shipping")
    assert product.buy(1) == 10.0
    with pytest.raises(ValueError):
        product.buy(2)  # Exceeds maximum purchase limit
