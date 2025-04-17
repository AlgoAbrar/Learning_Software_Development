#multiple inheritance

class Vehicle:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    

    def __repr__(self)-> str:
        return f"Brand: {self.brand}, Price: {self.price}"
    def move(self):
        pass

class Bus(Vehicle):
    def __init__(self,name,price,seat)->None:
        super().__init__(name,price)
        self.seat = seat
    
    def __repr__(self)->str:
        print(f"Brand: {self.brand}, Price: {self.price}, Seat: {self.seat}")
        return super().__repr__()

class truck(Vehicle):
    def __init__(self, brand, price,weight)->None:
        super().__init__(brand, price)
        self.weight = weight

class pickup(truck):
    def __init__(self, brand, price, weight)->None:
        super().__init__(brand, price, weight)
    

    def __repr__(self)-> str:
        return f'pickup: {self.brand} {self.price} {self.weight} {self.color}'
    
greenline= Bus('greenline', 120000, 50)
print(greenline)