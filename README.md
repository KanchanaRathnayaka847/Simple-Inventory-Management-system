# Web-Based Simple Inventory Management System

A comprehensive web-based inventory management system developed in Python (Flask) for small businesses.

## 📘 1. Project Overview

This project is a web-based inventory management system developed in Python (Flask). It allows small business owners, such as shopkeepers or salon owners, to record purchases and sales, track available stock, and calculate total inventory value — all through a simple web interface.

Currently, the system stores data in a JSON file, but it can be easily extended to use a database (e.g., SQLite, MySQL, or PostgreSQL) when handling larger volumes of data or multi-user access.

## ⚙️ 2. Problem Description

Small businesses often manage their inventory manually — using paper records or spreadsheets. This approach creates several challenges:

- Difficulty in tracking stock quantities accurately
- Risk of data loss or calculation errors
- No real-time view of available inventory or total value
- Time-consuming manual updates

These issues can lead to overstocking, undersupply, or loss of profit visibility.

## 💡 3. How the Program Solves the Problem

This application simplifies inventory management by digitalizing the process:

- Users can record purchases (new stock) or process sales easily via web forms
- The system automatically updates quantities in real time
- Each transaction (purchase/sale) instantly updates the JSON file, maintaining data consistency
- It provides an inventory summary, showing all products, available quantities, and total inventory value

While simple, it demonstrates how automation replaces manual tracking with structured, error-free digital data.

## 🔍 4. Aspects of the Problem Solved by the Program

| Problem Aspect | How the Program Solves It |
|----------------|---------------------------|
| Manual stock tracking | Centralized digital inventory list |
| Calculation errors | Automated quantity and total value computation |
| No quick stock overview | Real-time product list and inventory summary |
| Paper-based logs | Persistent data storage in a JSON file |

## 🔄 5. How Solving the Problem Changes the Process

| Old Process | New Process (Using the Program) |
|-------------|----------------------------------|
| Manual purchase/sales entry on paper | Record through web form |
| Calculations done by hand | Auto-calculated totals and stock levels |
| Separate files per day | Centralized, continuous record in JSON |
| No alerts or feedback | Flash messages confirm each operation instantly |

## 🧱 6. Requirements the Solution Places on the Program

To achieve its functionality, the system must:

- Store data persistently (via JSON file)
- Provide a user-friendly web interface for both purchases and sales
- Perform accurate arithmetic operations on quantities and prices
- Prevent errors, such as selling more than the available stock
- Run locally without a separate database or cloud service

**Scalability note:** If more users, data, or reporting features are added in the future, a database (like SQLite or MySQL) can replace the JSON storage for better performance and reliability.

## 🧩 7. How the Program Changes the Original Operating Model

Originally, businesses manually updated notebooks or Excel sheets. Now, this program acts as a local digital assistant:

- Every sale or purchase updates the central JSON record instantly
- Data is retrievable anytime through the browser interface
- Manual recalculations are eliminated

This transition improves efficiency, accuracy, and visibility in day-to-day operations.

## 🧰 8. Usage Scenarios

The program is ideal for small-scale, local businesses such as:

- Hair salons
- Grocery or convenience shops
- Cafés or local restaurants
- Home-based businesses managing small inventories

It is especially useful where database setup would be too complex or unnecessary. However, if the business grows, it can easily migrate to a database-based model.

## 🌐 9. Technical Requirements and Execution

| Requirement | Description |
|-------------|-------------|
| Language | Python 3 |
| Framework | Flask |
| Storage | JSON file (inventory_data.json) |
| Execution | Local server (localhost:5000) |
| Hardware | Any device capable of running Python |
| Deployment | Local only (no internet/server dependency) |

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

3. **Run the system**
   ```bash
   python app.py
   ```

4. **Open your browser and go to:**
   ```
   http://localhost:5000
   ```

## 🏗️ 10. Software Architecture

The system uses a simple two-layer architecture:

```
Frontend (HTML templates)
           ↓
Backend (Flask + Python logic)
           ↓
Storage (JSON file)
```

### Key Components:

- **Flask routes** handle web requests and responses
- **WebInventoryManager class** performs logic for adding purchases, processing sales, and updating stock
- **JSON file** stores inventory data persistently

The architecture can later be extended to include a database layer for advanced data management. This structure is chosen for clarity, simplicity, and easy explanation — perfect for educational and small-scale use.

## 🧪 11. Ensuring Correct Functioning

The following design choices help maintain reliability:

- **Input validation**: Prevents invalid or negative quantities
- **Error handling**: Catches missing products and file errors
- **Flash messages**: Provides instant feedback after each transaction
- **JSON integrity**: Every update re-saves the file cleanly with indentation

### Testing was performed by:

- Adding new products and verifying their appearance in inventory
- Performing sales and confirming that quantities and totals update correctly
- Restarting the app to ensure data persistence through JSON

## 🧭 12. Usability Considerations

The system emphasizes simplicity and clarity:

- Clean, intuitive forms for purchases and sales
- Visual table view of all products and total inventory value
- Instant feedback messages for user actions
- Minimal setup — only one command to start the system

Even a non-technical user (like a small business owner) can operate it with no prior training.

## 🧠 13. How to Use the Program

1. **Start the app** using `python app.py`
2. **Open the browser** at `http://localhost:5000`
3. **Navigate via the home page** to:
   - **Record Purchase**: Add new or update existing stock
   - **Record Sale**: Process sales and reduce quantities
   - **View Inventory**: See all products, total items, and total value
4. **The app automatically saves** changes in `inventory_data.json`

## ✨ Features

- 📊 **View Inventory**: Interactive dashboard with real-time statistics
- 📥 **Record Purchases**: Smart forms for adding products and stock
- 📤 **Process Sales**: Automated inventory updates with validation
- 📱 **Mobile Friendly**: Responsive design works on all devices
- 💾 **Data Persistence**: Automatic saving to JSON database
- 🎨 **Modern UI**: Professional interface with Bootstrap styling

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

## 🚀 14. Future Improvements

While this version focuses on simplicity, it can be expanded with:

- **User authentication** (to manage staff access)
- **Reports and analytics** (sales trends, daily profit summary)
- **Database integration** (for scalability and multi-user support)
- **Barcode scanning support** for quick entry
- **Export options** (CSV or Excel report generation)
- **Cloud-based deployment** for remote access

## 🛠️ Technology Stack

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Bootstrap 5, Font Awesome
- **Database**: JSON file storage
- **Real-time**: AJAX for dynamic updates

## 👩‍💻 15. Author

**Kanchana Madushani**  
ERP Student – Centria University of Applied Sciences

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

---

*Built with ❤️ using Python Flask*