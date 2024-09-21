# Retail Inventory Management System

## Overview

This is a Command Line Interface (CLI) application designed for managing inventory, suppliers, and orders in a small retail business. The system allows users to add and manage products, suppliers, and track orders efficiently using an SQLite database.

---

## Features

- **Inventory Management**: 
  - Add new products.
  - Update stock levels for existing products.
  - List all products in the inventory.

- **Supplier Management**:
  - Add new suppliers.
  - List all suppliers.

- **Order Management**:
  - Place new orders to restock products.
  - List all orders.

---

## Project Structure

```bash
retail_inventory_management/
│
├── cli/
│   ├── inventory_cli.py       # CLI commands for inventory management
│   ├── supplier_cli.py        # CLI commands for supplier management
│   ├── order_cli.py           # CLI commands for order management
│   ├── __init__.py
│
├── models/
│   ├── __init__.py
│   ├── inventory.py           # SQLAlchemy model for Inventory
│   ├── supplier.py            # SQLAlchemy model for Supplier
│   ├── order.py               # SQLAlchemy model for Order
│
├── db/
│   ├── database.py            # Database setup with SQLAlchemy
│   ├── init_db.py             # Script to initialize the database
│
├── Pipfile                    # Python environment and dependencies
├── Pipfile.lock
├── README.md                  # Project documentation
└── manage.py                  # Main CLI entry point

Usage
All commands for managing inventory, suppliers, and orders are handled through the CLI.

Available Commands:
1. Supplier Commands
Add a supplier:
bash
Copy code
pipenv run python manage.py supplier add "Supplier Name" "Contact Info"
List all suppliers:
bash
Copy code
pipenv run python manage.py supplier list
2. Inventory Commands
Add a product:

bash
Copy code
pipenv run python manage.py inventory add "Product Name" Stock_Level Price "Supplier Name"
List all products:

bash
Copy code
pipenv run python manage.py inventory list
Update product stock:

bash
Copy code
pipenv run python manage.py inventory update-stock "Product Name" New_Stock_Level
3. Order Commands
Place an order:

bash
Copy code
pipenv run python manage.py order place "Product Name" "Supplier Name" Quantity "Order Date"
List all orders:

bash
Copy code
pipenv run python manage.py order list
How It Works
This application uses:

SQLAlchemy ORM to manage the interaction with an SQLite database.
Click to create a powerful, yet simple CLI for managing the inventory system.
SQLite to store data locally in inventory.db.
Future Enhancements
Add support for reports (e.g., stock reports, sales reports).
Add more granular product categories.
Implement role-based access for different users.
License
This project is licensed under the MIT License.


