from product import Product

class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

class Customer(User):
    def __init__(self, email, password):
        super().__init__(email, password)
        self.cart = []
        self.orders = []

    def add_to_cart(self, product, quantity):
        self.cart.append((product, quantity))

    def clear_cart(self):
        self.cart = []

class Seller(User):
    def __init__(self, email, password):
        super().__init__(email, password)
        self.products = []

    def add_product(self, store, name, price, stock):
        product = Product(name, price, stock, self)
        self.products.append(product)
        store.add_product(product)

class Admin(User):
    def __init__(self, email, password):
        super().__init__(email, password)
