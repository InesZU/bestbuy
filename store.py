import products


class Store:
    def __init__(self, product: object) -> object:
        self.products = product

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self, product_list) -> int:
        total_quantity = sum(product.get_quantity() for product in self.products)
        return total_quantity

    def get_all_products(self) -> list[products.Product]:
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list) -> float:
        total_price = 0.0
        for product, quantity in shopping_list:
            product in self.products and product.is_active()
            total_price += product.buy(quantity)
        return total_price


if __name__ == "__main__":
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    ]

    store = Store(product_list)
    products = store.get_all_products()
    print(store.get_total_quantity())
    print(store.order([(products[0], 1), (products[1], 2)]))
