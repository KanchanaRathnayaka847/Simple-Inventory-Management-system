#!/usr/bin/env python3
"""
Web-based Simple Inventory Management System
Flask web application for inventory management with browser interface

Author: Kanchana Madushani
Institution: Centria University of Applied Sciences
"""

# Import required libraries
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import json
import os
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change in production

class WebInventoryManager:
    """Handles all inventory operations - loading, saving, purchases, and sales"""
    
    def __init__(self):
        """Initialize inventory manager and load existing data"""
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
    
    def get_all_products(self):
        """Return all products in inventory"""
        return self.inventory
    
    def add_purchase(self, product_id, name=None, unit=None, price=None, quantity=None):
        """Add purchase to inventory - updates existing product or creates new one"""
        if product_id in self.inventory:
            # Update existing product quantity
            self.inventory[product_id]['quantity'] += float(quantity)
            return f"Updated {self.inventory[product_id]['name']} - New quantity: {self.inventory[product_id]['quantity']} {self.inventory[product_id]['unit']}"
        else:
            # Create new product entry
            self.inventory[product_id] = {
                'name': name,
                'unit': unit,
                'price': float(price),
                'quantity': float(quantity)
            }
            return f"Added new product: {name}"
    
    def process_sale(self, product_id, quantity):
        """Process sale transaction - validates stock and updates inventory"""
        # Check if product exists
        if product_id not in self.inventory:
            return False, "Product not found in inventory"
        
        product = self.inventory[product_id]
        sale_quantity = float(quantity)
        
        # Validate quantity
        if sale_quantity <= 0:
            return False, "Sale quantity must be positive"
        
        if sale_quantity > product['quantity']:
            return False, f"Insufficient stock! Available: {product['quantity']} {product['unit']}"
        
        # Process sale
        self.inventory[product_id]['quantity'] -= sale_quantity
        total_sale_value = sale_quantity * product['price']
        
        result_message = f"Sold: {sale_quantity} {product['unit']} of {product['name']} for ${total_sale_value:.2f}"
        
        # Remove product if quantity reaches zero
        if self.inventory[product_id]['quantity'] == 0:
            del self.inventory[product_id]
            result_message += " (Product removed - quantity reached 0)"
        
        return True, result_message

# Create inventory manager instance
inventory_manager = WebInventoryManager()

# Flask routes
@app.route('/')
def index():
    """Display home page with navigation"""
    return render_template('index.html')

@app.route('/inventory')
def view_inventory():
    """Display inventory table with statistics"""
    products = inventory_manager.get_all_products()
    total_products = len(products)
    total_value = sum(p['price'] * p['quantity'] for p in products.values())
    return render_template('inventory.html', 
                         products=products, 
                         total_products=total_products,
                         total_value=total_value)

@app.route('/purchase', methods=['GET', 'POST'])
def record_purchase():
    """Handle purchase form display and processing"""
    if request.method == 'POST':
        # Process purchase form
        product_id = request.form['product_id'].strip()
        quantity = request.form['quantity']
        
        try:
            if product_id in inventory_manager.inventory:
                # Existing product - add quantity
                message = inventory_manager.add_purchase(product_id, quantity=quantity)
                inventory_manager.save_data()
                flash(message, 'success')
            else:
                # New product - get all details
                name = request.form['name'].strip()
                unit = request.form['unit'].strip()
                price = request.form['price']
                
                message = inventory_manager.add_purchase(product_id, name, unit, price, quantity)
                inventory_manager.save_data()
                flash(message, 'success')
            
            return redirect(url_for('record_purchase'))
        
        except ValueError as e:
            flash(f"Error: Invalid input - {str(e)}", 'error')
        except Exception as e:
            flash(f"Error: {str(e)}", 'error')
    
    # Display purchase form
    existing_products = inventory_manager.get_all_products()
    return render_template('purchase.html', existing_products=existing_products)

@app.route('/sale', methods=['GET', 'POST'])
def record_sale():
    """Handle sales form display and processing"""
    if request.method == 'POST':
        # Process sale form
        product_id = request.form['product_id']
        quantity = request.form['quantity']
        
        try:
            success, message = inventory_manager.process_sale(product_id, quantity)
            
            if success:
                inventory_manager.save_data()
                flash(message, 'success')
            else:
                flash(message, 'error')
            
            return redirect(url_for('record_sale'))
        
        except ValueError as e:
            flash(f"Error: Invalid quantity - {str(e)}", 'error')
        except Exception as e:
            flash(f"Error: {str(e)}", 'error')
    
    # Display sales form
    available_products = inventory_manager.get_all_products()
    return render_template('sale.html', available_products=available_products)

@app.route('/api/product/<product_id>')
def get_product_info(product_id):
    """API endpoint to get product information as JSON for form updates"""
    inventory_manager.load_data()
    
    if product_id in inventory_manager.inventory:
        return jsonify(inventory_manager.inventory[product_id])
    else:
        return jsonify({'error': 'Product not found'}), 404

# Main application startup
if __name__ == '__main__':
    """Run the Flask application"""
    # Create required directories
    os.makedirs('templates', exist_ok=True)
    os.makedirs('static/css', exist_ok=True)
    
    # Display startup info
    print("Starting Simple Inventory Management System (Web Version)")
    print("Open your browser and go to: http://localhost:5000")
    
    # Start Flask server
    app.run(debug=True, host='0.0.0.0', port=5000)