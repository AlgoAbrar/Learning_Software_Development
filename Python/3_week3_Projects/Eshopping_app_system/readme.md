# E-Shop Python Application

## Introduction
This is a simple e-commerce application built in Python. It allows customers to register, log in, view products, add them to their cart, and place orders. Admins can manage users, view products, and add or remove products. The application is structured using Object-Oriented Programming (OOP) principles for better organization and scalability.

## Features

- **Customer**:
  - Register and log in
  - View available products
  - Add products to cart
  - View cart
  - Place orders
  
- **Admin**:
  - Register and log in
  - View all users and products
  - Add, remove, and view products
  - Register and remove admins

## Project Structure
The project is organized into different files for modularity and better code reusability:
- `main.py`: The main entry point for the application.
- `store.py`: Contains the `Store` class, which holds all the logic for managing products, customers, and admins.
- `product.py`: Defines the `Product` class.
- `user.py`: Defines the `User`, `Customer`, `Seller`, and `Admin` classes.
- `admin.py`: Contains the `AdminManager` class for managing admin operations.
- `customer.py`: Contains the `CustomerManager` class for customer operations.

## Predefined Products
Six predefined products are added to the store for testing:
1. Laptop
2. Mouse
3. Keyboard
4. Monitor
5. Smartphone
6. Headphone

## Setup Instructions

### Requirements
- Python 3.x (preferably 3.7+)

### Installation
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/eshop.git
   cd eshop
