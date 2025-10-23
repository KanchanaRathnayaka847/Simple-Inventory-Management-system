# Simple Inventory Management System

A Python-based inventory management system that allows you to track product inventory, record purchases, and record sales.

## Features

- **View Total Inventory**: Display all products with ID, name, measuring unit, price, and quantity
- **Record Purchases**: Add new products or increase quantity of existing products
- **Record Sales**: Decrease inventory quantity when products are sold
- **Data Persistence**: All data is saved to a JSON file for persistence between sessions

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses only built-in Python modules)

## Installation

1. Clone this repository or download the files
2. Navigate to the project directory
3. Run the application:

```bash
python main.py
```

## Usage

### Main Menu Options

1. **View Total Inventory**
   - Displays all products in a formatted table
   - Shows Product ID, Name, Unit, Price, and Quantity

2. **Record Purchase**
   - For existing products: Enter Product ID and quantity to add
   - For new products: Enter all product details (ID, name, unit, price, quantity)
   - Inventory quantity increases automatically

3. **Record Sale**
   - Enter Product ID and quantity to sell
   - System checks if sufficient stock is available
   - Inventory quantity decreases automatically
   - Products are removed when quantity reaches 0

4. **Exit**
   - Saves all data and closes the application

### Data Structure

Each product in the inventory contains:
- **Product ID**: Unique identifier
- **Product Name**: Name of the product
- **Measuring Unit**: Unit of measurement (kg, pcs, liters, etc.)
- **Price**: Price per unit
- **Quantity**: Current stock quantity

### Data Storage

- All inventory data is stored in `inventory_data.json`
- Data is automatically saved after each purchase or sale
- The JSON file is created automatically on first run

## Example Usage

```
=================================================
        INVENTORY MANAGEMENT SYSTEM
=================================================
1. View Total Inventory
2. Record Purchase
3. Record Sale
4. Exit
-------------------------------------------------
Enter your choice (1-4): 2

==================================================
               RECORD PURCHASE
==================================================
Enter Product ID: P001
New Product - Please enter details:
Product Name: Apples
Measuring Unit (e.g., kg, pcs, liters): kg
Price per unit: $2.50
Purchase quantity (kg): 10
Added new product to inventory: Apples
Purchase recorded successfully!
```

## File Structure

```
inventory-management-system/
├── main.py                 # Main application file
├── inventory_data.json     # Data storage file (created automatically)
└── README.md              # This documentation file
```

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is open source and available under the MIT License.