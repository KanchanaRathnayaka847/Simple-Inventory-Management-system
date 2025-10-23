# Simple Inventory Management System

A modern web-based inventory management system built with Python Flask.

## ✨ Features

- 📊 **View Inventory**: Interactive dashboard with real-time statistics
- 📥 **Record Purchases**: Smart forms for adding products and stock
- 📤 **Process Sales**: Automated inventory updates with validation
- 📱 **Mobile Friendly**: Responsive design works on all devices
- 💾 **Data Persistence**: Automatic saving to JSON database
- 🎨 **Modern UI**: Professional interface with Bootstrap styling

## 🚀 Quick Start

### Prerequisites
- Python 3.6+
- Web browser

### Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/KanchanaRathnayaka847/Simple-Inventory-Management-system.git
   cd Simple-Inventory-Management-system
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open in browser**
   ```
   http://localhost:5000
   ```

## 📱 How to Use

### Dashboard
- View total inventory count and value
- Monitor stock levels with visual indicators
- Access all features from the main navigation

### Adding Products
1. Click "Record Purchase"
2. Enter product details or select existing product
3. Specify quantity to add
4. Submit to update inventory

### Recording Sales
1. Click "Record Sale"
2. Select product from dropdown
3. Enter sale quantity
4. System validates stock availability
5. Inventory updates automatically

## 🛠️ Technology Stack

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Bootstrap 5, Font Awesome
- **Database**: JSON file storage
- **Real-time**: AJAX for dynamic updates

## 📁 Project Structure

```
inventory-management-system/
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── templates/                  # HTML templates
│   ├── base.html              # Base layout
│   ├── index.html             # Dashboard
│   ├── inventory.html         # Inventory view
│   ├── purchase.html          # Purchase form
│   └── sale.html              # Sales form
├── static/css/                # Styling
│   └── style.css              # Custom CSS
├── sample_inventory_data.json  # Example data
└── README.md                  # Documentation
```

## 📄 License

[Add your license information here]

## 👨‍💻 Author

[Add your information here]

## 🤝 Contributing

[Add contribution guidelines here]

---

*Built with ❤️ using Python Flask*