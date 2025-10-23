#!/usr/bin/env python3
"""
Simple Inventory Management System
This system allows you to:
1. View total inventory
2. Record purchases (increases inventory)
3. Record sales (decreases inventory)
"""

import json
import os
from datetime import datetime

class InventoryManager:
    def __init__(self):
        self.data_file = "inventory_data.json"
        self.load_data()
    
    def load_data(self):
        """Load inventory data from JSON file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as file:
                    self.inventory = json.load(file)
            except (json.JSONDecodeError, FileNotFoundError):
                self.inventory = {}
        else:
            self.inventory = {}
    
    def save_data(self):
        """Save inventory data to JSON file"""
        with open(self.data_file, 'w') as file:
            json.dump(self.inventory, file, indent=2)
    
    def display_inventory(self):
        """Display total inventory in a formatted table"""
        print("\n" + "="*80)
        print("                          TOTAL INVENTORY")
        print("="*80)
        
        if not self.inventory:
            print("No products in inventory.")
            return
        
        # Table header
        print(f"{'ID':<8} {'Product Name':<20} {'Unit':<10} {'Price':<10} {'Quantity':<10}")
        print("-" * 80)
        
        # Table rows
        for product_id, product in self.inventory.items():
            print(f"{product_id:<8} {product['name']:<20} {product['unit']:<10} "
                  f"${product['price']:<9.2f} {product['quantity']:<10}")
        
        print("-" * 80)
        print(f"Total Products: {len(self.inventory)}")
    
    def record_purchase(self):
        """Record a purchase and update inventory"""
        print("\n" + "="*50)
        print("               RECORD PURCHASE")
        print("="*50)
        
        product_id = input("Enter Product ID: ").strip()
        
        if product_id in self.inventory:
            # Existing product
            print(f"Existing Product: {self.inventory[product_id]['name']}")
            quantity = float(input(f"Enter quantity to purchase ({self.inventory[product_id]['unit']}): "))
            
            # Update existing product
            self.inventory[product_id]['quantity'] += quantity
            print(f"Updated inventory. New quantity: {self.inventory[product_id]['quantity']} {self.inventory[product_id]['unit']}")
        else:
            # New product
            print("New Product - Please enter details:")
            name = input("Product Name: ").strip()
            unit = input("Measuring Unit (e.g., kg, pcs, liters): ").strip()
            price = float(input("Price per unit: $"))
            quantity = float(input(f"Purchase quantity ({unit}): "))
            
            # Add new product to inventory
            self.inventory[product_id] = {
                'name': name,
                'unit': unit,
                'price': price,
                'quantity': quantity
            }
            print(f"Added new product to inventory: {name}")
        
        self.save_data()
        print("Purchase recorded successfully!")
    
    def record_sale(self):
        """Record a sale and update inventory"""
        print("\n" + "="*50)
        print("                RECORD SALE")
        print("="*50)
        
        if not self.inventory:
            print("No products in inventory to sell.")
            return
        
        product_id = input("Enter Product ID to sell: ").strip()
        
        if product_id not in self.inventory:
            print("Product not found in inventory.")
            return
        
        product = self.inventory[product_id]
        print(f"Product: {product['name']}")
        print(f"Available quantity: {product['quantity']} {product['unit']}")
        print(f"Price per unit: ${product['price']:.2f}")
        
        try:
            sale_quantity = float(input(f"Enter quantity to sell ({product['unit']}): "))
            
            if sale_quantity <= 0:
                print("Sale quantity must be positive.")
                return
            
            if sale_quantity > product['quantity']:
                print(f"Insufficient stock! Available: {product['quantity']} {product['unit']}")
                return
            
            # Update inventory
            self.inventory[product_id]['quantity'] -= sale_quantity
            total_sale_value = sale_quantity * product['price']
            
            print(f"Sale recorded successfully!")
            print(f"Sold: {sale_quantity} {product['unit']} of {product['name']}")
            print(f"Sale value: ${total_sale_value:.2f}")
            print(f"Remaining quantity: {self.inventory[product_id]['quantity']} {product['unit']}")
            
            # Remove product if quantity becomes 0
            if self.inventory[product_id]['quantity'] == 0:
                del self.inventory[product_id]
                print("Product removed from inventory (quantity reached 0).")
            
            self.save_data()
            
        except ValueError:
            print("Invalid quantity entered.")
    
    def display_menu(self):
        """Display main menu"""
        print("\n" + "="*50)
        print("        INVENTORY MANAGEMENT SYSTEM")
        print("="*50)
        print("1. View Total Inventory")
        print("2. Record Purchase")
        print("3. Record Sale")
        print("4. Exit")
        print("-" * 50)
    
    def run(self):
        """Main application loop"""
        print("Welcome to Simple Inventory Management System!")
        
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-4): ").strip()
            
            if choice == '1':
                self.display_inventory()
            elif choice == '2':
                self.record_purchase()
            elif choice == '3':
                self.record_sale()
            elif choice == '4':
                print("Thank you for using Inventory Management System!")
                break
            else:
                print("Invalid choice. Please enter 1-4.")
            
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    manager = InventoryManager()
    manager.run()