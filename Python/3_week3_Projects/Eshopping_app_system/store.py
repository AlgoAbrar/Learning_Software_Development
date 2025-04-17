from user import Customer, Seller, Admin

class Store:
    def __init__(self):
        self.customers = []
        self.sellers = []
        self.products = []
        self.admins = [Admin("Abrar", "Abrarboss123")]

    def register_customer(self, email, password):
        customer = Customer(email, password)
        self.customers.append(customer)
        return customer

    def register_seller(self, email, password):
        seller = Seller(email, password)
        self.sellers.append(seller)
        return seller

    def login_customer(self, email, password):
        for customer in self.customers:
            if customer.email == email and customer.password == password:
                return customer
        return None

    def login_seller(self, email, password):
        for seller in self.sellers:
            if seller.email == email and seller.password == password:
                return seller
        return None

    def login_admin(self, email, password):
        for admin in self.admins:
            if admin.email == email and admin.password == password:
                return admin
        return None

    def add_product(self, product):
        self.products.append(product)

    def get_available_products(self):
        return [p for p in self.products if p.stock > 0]

    def place_order_from_cart(self, customer):
        for product, quantity in customer.cart:
            if product.stock >= quantity:
                product.reduce_stock(quantity)
                customer.orders.append((product, quantity))
        customer.clear_cart()
        return "Order placed successfully!"
