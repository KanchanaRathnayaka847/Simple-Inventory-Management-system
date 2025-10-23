# Simple Inventory Management System

A Python-based inventory management system with both **console** and **web** interfaces that allows you to track product inventory, record purchases, and record sales.

## 🌟 Features

- **View Total Inventory**: Display all products with ID, name, measuring unit, price, and quantity
- **Record Purchases**: Add new products or increase quantity of existing products
- **Record Sales**: Decrease inventory quantity when products are sold
- **Data Persistence**: All data is saved to a JSON file for persistence between sessions
- **Web Interface**: Modern, responsive web interface accessible through any browser
- **Real-time Updates**: Dynamic calculations and stock validation
- **Mobile Friendly**: Responsive design works on desktop, tablet, and mobile devices

## 📋 Requirements

- Python 3.6 or higher
- Flask 3.0.0 (for web interface)
- Modern web browser (for web interface)

## 🚀 Installation

1. Clone this repository:
```bash
git clone https://github.com/KanchanaRathnayaka847/Simple-Inventory-Management-system.git
cd Simple-Inventory-Management-system
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Choose your interface:

### Console Version
```bash
python main.py
```

### Web Version (Recommended)
```bash
python app.py
```
Then open your browser and go to: **http://localhost:5000**

## 💻 Usage

### Web Interface (Recommended)

The web interface provides a modern, user-friendly experience with:

1. **Home Dashboard**: Overview of system features and quick navigation
2. **Inventory View**: 
   - Interactive table with all products
   - Real-time stock status indicators
   - Total inventory value calculations
   - Low stock warnings
3. **Purchase Recording**: 
   - Smart form that detects existing products
   - Auto-complete for product details
   - Quantity validation
4. **Sales Processing**: 
   - Product selection dropdown
   - Real-time sale calculations
   - Stock availability validation

### Console Interface

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

## 📱 Screenshots & Demo

### Web Interface
- **Home Page**: Clean dashboard with feature overview
- **Inventory View**: Professional table with status indicators
- **Purchase Form**: Smart form with existing product detection
- **Sales Form**: Real-time calculations and validation

Access the web interface at: `http://localhost:5000`

## 🗂️ File Structure

```
inventory-management-system/
├── app.py                  # Flask web application
├── main.py                 # Console application
├── requirements.txt        # Python dependencies
├── inventory_data.json     # Data storage (created automatically)
├── templates/              # HTML templates for web interface
│   ├── base.html          # Base template with navigation
│   ├── index.html         # Home page
│   ├── inventory.html     # Inventory view page
│   ├── purchase.html      # Purchase recording page
│   └── sale.html          # Sales recording page
├── static/
│   └── css/
│       └── style.css      # Custom CSS styling
├── sample_inventory_data.json  # Sample data for reference
└── README.md              # Documentation
```

## 🔧 Configuration

### Web Server Settings
- **Host**: 0.0.0.0 (accessible from any IP)
- **Port**: 5000
- **Debug Mode**: Enabled in development

### Security
- Change the `secret_key` in `app.py` for production use
- Consider using environment variables for sensitive configuration

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is open source and available under the MIT License.