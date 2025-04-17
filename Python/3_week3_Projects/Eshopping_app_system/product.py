class Product:
    def __init__(self, name, price, stock, seller):
        self.name = name
        self.price = price
        self.stock = stock
        self.seller = seller

    def reduce_stock(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            return True
        return False
