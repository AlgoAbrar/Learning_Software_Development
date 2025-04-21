class Bus:
    def __init__(self, number, route, total_seats):
        self.number = number
        self.route = route
        self.total_seats = total_seats
        self.booked_seats = 0

    def available_seats(self):
        return self.total_seats-self.booked_seats

    def book_seat(self):
        if self.available_seats() > 0:
            self.booked_seats += 1
            return True
        return False


class Passenger:
    def __init__(self, name, phone, bus):
        self.name=name
        self.phone=phone
        self.bus=bus

class Admin:
    def __init__(self, username, password):
        self.username=username
        self.password=password

    def login(self, username, password):
        return self.username == username, self.password == password

class BusSystem:
    def __init__(self):
        self.buses = []
        self.passengers = []
        self.admin=Admin("admin", "1234")

    def add_bus(self, number, route, seats):
        self.buses.append(Bus(number, route, seats))
        
    def find_bus(self, bus_number):
        for bus in self.buses:
            if bus.number == bus_number:
                return bus
        return None

    def book_ticket(self, bus_number, name, phone):
        bus = self.find_bus(bus_number)
        if not bus:
           print("Bus not found.")
           return None
        if bus.book_seat():
            passenger = Passenger(name, phone, bus)
            self.passengers.append(passenger)
            print(f"Ticket booked for {name}. vara 500 taka")
        else:
            print("No seats.")

    def show_buses(self):
        if not self.buses:
            print("No bus available.")
            return
        print("\nAvailable Bus:")
        for bus in self.buses:
            print(f"Bus No: {bus.number}, Route: {bus.route}, Seats Left: {bus.available_seats()}/{bus.total_seats}")

buss = BusSystem()
buss.add_bus("101", "Rajshahi", 54)
buss.add_bus("102", "Dhaka", 54)
buss.add_bus("103", "Chittagong", 54)

def admin_menu():
    while True:
        print("\nThe Great Admin Jhankar Mamma")
        print("1.Add Bus")
        print("2.View All Buses")
        print("3.Logout")
        choice = int(input("Enter choice: "))

        if choice == 1:
            number = input("Enter bus no.: ")
            route = input("Enter route: ")
            seats = int(input("Enter total seats: "))
            buss.add_bus(number, route, seats)
            print("Bus added.")
        elif choice == 2:
            buss.show_buses()
        elif choice == 3:
            print("Log out.")
            break
        else:
            print("Invalid input.")

while True:
    print("\nJhankar Mama Ticket Cutting System")
    print("1.Admin Login")
    print("2.Book Ticket")
    print("3.View Buses")
    print("4.Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        username = input("admin username: ")
        password = input("admin password: ")
        if buss.admin.login(username, password):
            print("Login successful.")
            admin_menu()
        else:
            print("Invalid.")
    elif choice == 2:
        if not buss.buses:
            print("No bus available.")
        else:
            bus_number = input("Enter bus number: ")
            name = input("Enter your name: ")
            phone = input("Enter your phone number: ")
            buss.book_ticket(bus_number, name, phone)
    elif choice == 3:
        buss.show_buses()
    elif choice == 4:
        print("Thank you mamma...")
        break
    else:
        print("Invalid input mamma....")
