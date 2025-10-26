#!/usr/bin/env python3
"""
Web-based Simple Inventory Management System
Flask web application for inventory management with browser interface

This application provides a complete web-based solution for small businesses
to manage their inventory through a user-friendly web interface.

Author: Kanchana Madushani
Institution: Centria University of Applied Sciences
Course: ERP Systems
"""

# Import necessary Flask components and standard Python libraries
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import json  # For handling JSON data storage
import os    # For file system operations
from datetime import datetime  # For timestamp functionality (future use)

# Initialize Flask application instance
app = Flask(__name__)

# Set secret key for session management and flash messages
# NOTE: In production, this should be a random, secure key stored as environment variable
app.secret_key = 'your-secret-key-here'  # Change this in production

class WebInventoryManager:
    """
    Core class that handles all inventory management operations
    
    This class manages the business logic for:
    - Loading and saving inventory data from/to JSON file
    - Processing purchases (adding/updating products)
    - Processing sales (reducing quantities)
    - Validating operations to prevent errors
    """
    
    def __init__(self):
        """
        Initialize the inventory manager
        Sets up the data file path and loads existing inventory data
        """
        # Define the JSON file that will store all inventory data
        self.data_file = "inventory_data.json"
        
        # Load existing inventory data on startup
        self.load_data()
    
    def load_data(self):
        """
        Load inventory data from JSON file into memory
        
        This method:
        1. Checks if the data file exists
        2. Attempts to load JSON data from file
        3. Handles errors gracefully by initializing empty inventory
        4. Ensures the application never crashes due to file issues
        """
        if os.path.exists(self.data_file):
            try:
                # Open and read the JSON file
                with open(self.data_file, 'r') as file:
                    self.inventory = json.load(file)
            except (json.JSONDecodeError, FileNotFoundError):
                # If file is corrupted or missing, start with empty inventory
                self.inventory = {}
        else:
            # If no data file exists yet, initialize empty inventory
            self.inventory = {}
    
    def save_data(self):
        """
        Save current inventory data to JSON file
        
        This method:
        1. Writes the current inventory dictionary to JSON file
        2. Uses indentation for readable file format
        3. Ensures data persistence between application sessions
        """
        with open(self.data_file, 'w') as file:
            # Save with indent=2 for human-readable JSON format
            json.dump(self.inventory, file, indent=2)
    
    def get_all_products(self):
        """
        Retrieve all products from inventory
        
        Returns:
            dict: Complete inventory dictionary with all products
        """
        return self.inventory
    
    def add_purchase(self, product_id, name=None, unit=None, price=None, quantity=None):
        """
        Process a purchase transaction (adds stock to inventory)
        
        This method handles two scenarios:
        1. Existing product: Adds quantity to current stock
        2. New product: Creates new inventory entry with all details
        
        Args:
            product_id (str): Unique identifier for the product
            name (str, optional): Product name (required for new products)
            unit (str, optional): Measuring unit (required for new products)
            price (float, optional): Price per unit (required for new products)
            quantity (float): Quantity being purchased
            
        Returns:
            str: Success message describing the operation performed
        """
        if product_id in self.inventory:
            # CASE 1: Existing product - add to current quantity
            # Convert quantity to float to handle decimal values
            self.inventory[product_id]['quantity'] += float(quantity)
            
            # Return descriptive message about the update
            return f"Updated {self.inventory[product_id]['name']} - New quantity: {self.inventory[product_id]['quantity']} {self.inventory[product_id]['unit']}"
        else:
            # CASE 2: New product - create complete inventory entry
            self.inventory[product_id] = {
                'name': name,                    # Product name
                'unit': unit,                    # Measuring unit (kg, pcs, liters, etc.)
                'price': float(price),           # Price per unit
                'quantity': float(quantity)      # Current stock quantity
            }
            
            # Return confirmation message for new product
            return f"Added new product: {name}"
    
    def process_sale(self, product_id, quantity):
        """
        Process a sale transaction (reduces stock from inventory)
        
        This method handles the complete sales process with validation:
        1. Verifies product exists in inventory
        2. Validates sale quantity is positive and available
        3. Updates inventory quantities
        4. Calculates sale value
        5. Removes products with zero stock
        
        Args:
            product_id (str): Unique identifier for the product being sold
            quantity (str/float): Quantity being sold
            
        Returns:
            tuple: (success_boolean, message_string)
                - success_boolean: True if sale processed, False if error
                - message_string: Descriptive message about the operation
        """
        
        # VALIDATION 1: Check if product exists in inventory
        if product_id not in self.inventory:
            return False, "Product not found in inventory"
        
        # Get product details for processing
        product = self.inventory[product_id]
        
        # Convert quantity to float for calculations
        sale_quantity = float(quantity)
        
        # VALIDATION 2: Ensure quantity is positive
        if sale_quantity <= 0:
            return False, "Sale quantity must be positive"
        
        # VALIDATION 3: Check if sufficient stock is available
        if sale_quantity > product['quantity']:
            return False, f"Insufficient stock! Available: {product['quantity']} {product['unit']}"
        
        # PROCESS THE SALE: Update inventory quantity
        self.inventory[product_id]['quantity'] -= sale_quantity
        
        # CALCULATE: Total value of this sale
        total_sale_value = sale_quantity * product['price']
        
        # CREATE: Success message with sale details
        result_message = f"Sold: {sale_quantity} {product['unit']} of {product['name']} for ${total_sale_value:.2f}"
        
        # CLEANUP: Remove product if stock reaches zero
        if self.inventory[product_id]['quantity'] == 0:
            del self.inventory[product_id]
            result_message += " (Product removed - quantity reached 0)"
        
        # Return success with detailed message
        return True, result_message

# ============================================================================
# GLOBAL INSTANCE: Create single inventory manager for the entire application
# ============================================================================
inventory_manager = WebInventoryManager()

# ============================================================================
# FLASK ROUTES: Define URL endpoints and their corresponding functions
# ============================================================================

@app.route('/')
def index():
    """
    HOME PAGE ROUTE
    
    Displays the main dashboard with navigation options
    This is the landing page users see when they visit the application
    
    Returns:
        Rendered HTML template for the home page
    """
    return render_template('index.html')

@app.route('/inventory')
def view_inventory():
    """
    INVENTORY VIEW ROUTE
    
    Displays complete inventory in a table format with statistics
    
    This route:
    1. Retrieves all products from inventory
    2. Calculates summary statistics (total products, total value)
    3. Passes data to template for display
    
    Returns:
        Rendered HTML template with inventory data and statistics
    """
    # Get all products from inventory manager
    products = inventory_manager.get_all_products()
    
    # Calculate summary statistics
    total_products = len(products)
    
    # Calculate total inventory value (quantity × price for all products)
    total_value = sum(p['price'] * p['quantity'] for p in products.values())
    
    # Render template with data
    return render_template('inventory.html', 
                         products=products, 
                         total_products=total_products,
                         total_value=total_value)

@app.route('/purchase', methods=['GET', 'POST'])
def record_purchase():
    """
    PURCHASE RECORDING ROUTE
    
    Handles both displaying the purchase form (GET) and processing purchases (POST)
    
    GET Request: Shows the purchase form with existing products for reference
    POST Request: Processes new purchase and updates inventory
    
    This route handles two scenarios:
    1. Adding stock to existing products
    2. Creating new products with full details
    
    Returns:
        GET: Rendered purchase form template
        POST: Redirect to purchase page with success/error message
    """
    
    if request.method == 'POST':
        # ========================================================================
        # PROCESS PURCHASE FORM SUBMISSION
        # ========================================================================
        
        # Extract form data
        product_id = request.form['product_id'].strip()  # Remove whitespace
        quantity = request.form['quantity']
        
        try:
            if product_id in inventory_manager.inventory:
                # SCENARIO 1: Existing product - add quantity only
                message = inventory_manager.add_purchase(product_id, quantity=quantity)
                inventory_manager.save_data()  # Persist changes to JSON file
                flash(message, 'success')      # Show success message to user
            else:
                # SCENARIO 2: New product - collect all details
                name = request.form['name'].strip()
                unit = request.form['unit'].strip()
                price = request.form['price']
                
                # Add new product with complete information
                message = inventory_manager.add_purchase(product_id, name, unit, price, quantity)
                inventory_manager.save_data()  # Persist changes to JSON file
                flash(message, 'success')      # Show success message to user
            
            # Redirect to same page to show updated data (POST-Redirect-GET pattern)
            return redirect(url_for('record_purchase'))
        
        except ValueError as e:
            # Handle invalid numeric inputs (price, quantity)
            flash(f"Error: Invalid input - {str(e)}", 'error')
        except Exception as e:
            # Handle any other unexpected errors
            flash(f"Error: {str(e)}", 'error')
    
    # ========================================================================
    # DISPLAY PURCHASE FORM (GET request or after POST processing)
    # ========================================================================
    
    # Get existing products to show in form dropdown/reference
    existing_products = inventory_manager.get_all_products()
    
    # Render purchase form template with existing products data
    return render_template('purchase.html', existing_products=existing_products)

@app.route('/sale', methods=['GET', 'POST'])
def record_sale():
    """
    SALES RECORDING ROUTE
    
    Handles both displaying the sales form (GET) and processing sales (POST)
    
    GET Request: Shows sales form with available products
    POST Request: Processes sale transaction and updates inventory
    
    This route includes validation to prevent:
    - Selling non-existent products
    - Selling more than available stock
    - Invalid quantity values
    
    Returns:
        GET: Rendered sales form template
        POST: Redirect to sales page with success/error message
    """
    
    if request.method == 'POST':
        # ========================================================================
        # PROCESS SALES FORM SUBMISSION
        # ========================================================================
        
        # Extract form data
        product_id = request.form['product_id']
        quantity = request.form['quantity']
        
        try:
            # Process the sale through inventory manager
            # This returns a tuple: (success_boolean, message_string)
            success, message = inventory_manager.process_sale(product_id, quantity)
            
            if success:
                # SALE SUCCESSFUL: Save changes and show success message
                inventory_manager.save_data()  # Persist inventory changes
                flash(message, 'success')      # Green success message
            else:
                # SALE FAILED: Show error message (no changes to save)
                flash(message, 'error')        # Red error message
            
            # Redirect to same page to show updated data (POST-Redirect-GET pattern)
            return redirect(url_for('record_sale'))
        
        except ValueError as e:
            # Handle invalid quantity input (non-numeric values)
            flash(f"Error: Invalid quantity - {str(e)}", 'error')
        except Exception as e:
            # Handle any other unexpected errors
            flash(f"Error: {str(e)}", 'error')
    
    # ========================================================================
    # DISPLAY SALES FORM (GET request or after POST processing)
    # ========================================================================
    
    # Get all available products for the sales dropdown
    available_products = inventory_manager.get_all_products()
    
    # Render sales form template with available products
    return render_template('sale.html', available_products=available_products)

@app.route('/api/product/<product_id>')
def get_product_info(product_id):
    """
    API ENDPOINT: Get product information as JSON
    
    This RESTful API endpoint provides product data in JSON format
    Used by JavaScript on the frontend for dynamic form updates
    
    Use case: When user types/selects a product ID in purchase form,
    JavaScript calls this endpoint to get product details and pre-fill form fields
    
    Args:
        product_id (str): Product ID from URL parameter
        
    Returns:
        JSON response with either:
        - Product data (name, unit, price, quantity) if found
        - Error message with 404 status if not found
    """
    
    # Reload inventory data to ensure we have the latest information
    inventory_manager.load_data()  # Refresh from JSON file
    
    if product_id in inventory_manager.inventory:
        # Product found: return product data as JSON
        return jsonify(inventory_manager.inventory[product_id])
    else:
        # Product not found: return error with HTTP 404 status
        return jsonify({'error': 'Product not found'}), 404

# ============================================================================
# APPLICATION STARTUP: Main execution block
# ============================================================================

if __name__ == '__main__':
    """
    Main application startup block
    
    This block only runs when the script is executed directly
    (not when imported as a module)
    
    Tasks performed:
    1. Create necessary directories for templates and static files
    2. Display startup information to user
    3. Start the Flask development server
    """
    
    # Ensure required directories exist
    os.makedirs('templates', exist_ok=True)    # HTML templates directory
    os.makedirs('static/css', exist_ok=True)   # CSS files directory
    
    # Display startup information
    print("=" * 60)
    print("Starting Simple Inventory Management System (Web Version)")
    print("=" * 60)
    print("🌐 Open your browser and go to: http://localhost:5000")
    print("📱 The application is mobile-friendly and responsive")
    print("💾 All data is saved automatically in inventory_data.json")
    print("🔄 Press Ctrl+C to stop the server")
    print("=" * 60)
    
    # Start Flask development server
    app.run(
        debug=True,        # Enable debug mode for development
        host='0.0.0.0',    # Accept connections from any IP address
        port=5000          # Run on port 5000
    )