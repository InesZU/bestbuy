class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.active = True
        self.quantity = quantity
        self.price = price

    def get_quantity(self) -> float:
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity <= 0:
            self.deactivate()

    def is_active(self) -> bool:
        if self.active:
            return True
        else:
            return False

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self) -> str:
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity) -> float:
        if quantity <= 0:
            raise ValueError("Quantity to buy should be greater than zero.")
        if quantity > self.quantity:
            raise ValueError("Not enough quantity available.")

        self.quantity -= quantity
        total_price = self.price * quantity
        if self.quantity == 0:
            self.deactivate()
        return total_price

if __name__ == "__main__":
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())
    print(bose.show())
    print(mac.show())

    bose.set_quantity(1000)
    print(bose.show())


