class CustomerManager:
    def __init__(self, store):
        self.store = store

    def view_products(self):
        print("\nAvailable Products:")
        for idx, product in enumerate(self.store.get_available_products()):
            print(f"{idx + 1}. {product.name} - ৳{product.price} - Stock: {product.stock}")
        print()

    def add_to_cart(self, customer, product, quantity):
        customer.add_to_cart(product, quantity)
        print(f"Added {product.name} x{quantity} to cart.")

    def view_cart(self, customer):
        print("\nYour Cart:")
        if not customer.cart:
            print("Cart is empty.")
        else:
            for idx, (p, q) in enumerate(customer.cart):
                print(f"{idx + 1}. {p.name} x{q}")
        print()

    def place_order_from_cart(self, customer):
        if not customer.cart:
            print("Cart is empty.")
        else:
            result = self.store.place_order_from_cart(customer)
            print(f"{result}")
