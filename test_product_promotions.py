from products import Product, NonStockedProduct, LimitedProduct
from promotions import PercentageDiscount, SecondItemHalfPrice, Buy2Get1Free

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

# Sample testing
for product in product_list:
    print(product.show())
    if product.is_active():
        try:
            print(f"Total price for 2 units: €{product.buy(2):.2f}")
        except ValueError as e:
            print(e)
