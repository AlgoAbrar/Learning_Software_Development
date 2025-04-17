# This code is a simple e-commerce system with user registration, product management, and order placement functionalities.
# It includes classes for Store, User, Customer, Seller, and Admin, along with their respective methods for managing products and users.

from store import Store
from user import Customer, Seller, Admin
from admin import AdminManager
from customer import CustomerManager 

def customer_menu(store, customer):
    customer_manager = CustomerManager(store)

    while True:
        print("\n***Customer Menu***")
        print("1. View Products")
        print("2. Add Product to Cart")
        print("3. View Cart")
        print("4. Place Order from Cart")
        print("5. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            customer_manager.view_products()

        elif choice == "2":
            products = store.get_available_products()
            customer_manager.view_products() 
            try:
                index = int(input("Enter product number to add to cart: ")) - 1
                quantity = int(input("Enter quantity: "))
                if 0 <= index < len(products):
                    selected_product = products[index]
                    if selected_product.stock >= quantity:
                        customer_manager.add_to_cart(customer, selected_product, quantity)
                    else:
                        print("Not enough stock.")
                else:
                    print("Invalid product number.")
            except ValueError:
                print("Invalid input. Please enter numbers only.")

        elif choice == "3":
            customer_manager.view_cart(customer)

        elif choice == "4":
            customer_manager.place_order_from_cart(customer)

        elif choice == "5":
            print("Logged out.")
            break

        else:
            print("Invalid choice.")

def admin_menu(store, admin):
    admin_manager = AdminManager(store)

    while True:
        print("\n--- Admin Panel ---")
        print("1. View All Users")
        print("2. View All Products")
        print("3. Remove Product")
        print("4. Add Product")
        print("5. View All Admins")
        print("6. Register New Admin")
        print("7. Remove Registered Admin")
        print("8. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            admin.view_all_users(store)
        elif choice == "2":
            admin.view_all_products(store)
        elif choice == "3":
            admin.view_all_products(store)
            try:
                index = int(input("Enter product index to remove: ")) - 1
                admin.remove_product(store, index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            name = input("Product name: ")
            try:
                price = int(input("Price: "))
                stock = int(input("Stock: "))
                admin.add_product_as_admin(store, name, price, stock)
            except ValueError:
                print("Please enter valid numbers for price and stock.")
        elif choice == "5":
            admin_manager.view_all_admins()
        elif choice == "6":
            email = input("Enter new admin email: ")
            password = input("Enter new admin password: ")
            admin_manager.register_admin(email, password)
        elif choice == "7":
            admin_manager.view_all_admins()
            try:
                admin_index = int(input("Enter the index of admin to remove: ")) - 1
                admin_manager.remove_admin(admin_index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "8":
            print("Admin logged out.")
            break
        else:
            print("Invalid choice.")

store = Store()


seller = store.register_seller("abrar@gmail.com", "123456")
seller.add_product(store, "Laptop", 50000, 5)
seller.add_product(store, "Mouse", 500, 10)
seller.add_product(store, "Keyboard", 1500, 7)
seller.add_product(store, "Monitor", 10000, 3)
seller.add_product(store, "Smartphone", 25000, 15)
seller.add_product(store, "Headphone", 2000, 20)

# Main Loop
while True:
    print("\n=== Welcome to E-Shop ===")
    print("1. Register as Customer")
    print("2. Login as Customer")
    print("3. Login as Admin")
    print("4. Exit")

    main_choice = input("Choose an option: ")

    if main_choice == "1":
        email = input("Enter your email: ")
        password = input("Enter password: ")
        store.register_customer(email, password)
        print("Registration successful!")

    elif main_choice == "2":
        email = input("Enter email: ")
        password = input("Enter password: ")
        customer = store.login_customer(email, password)
        if customer:
            print(f"Login successful. Welcome {customer.email}!")
            customer_menu(store, customer)
        else:
            print("Login failed. Try again.")

    elif main_choice == "3":
        email = input("Admin Email: ")
        password = input("Admin Password: ")
        admin = store.login_admin(email, password)
        if admin:
            print("Welcome Admin!")
            admin_menu(store, admin)
        else:
            print("Invalid admin credentials.")

    elif main_choice == "4":
        print("Thank you for using E-Shop!")
        break

    else:
        print("Invalid option. Try again.")
