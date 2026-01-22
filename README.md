# 🥛 Kiran Dairy - Milk Billing Application

**Fresh Milk, Fair Price**

A simple and elegant web application for managing dairy milk billing with support for both cow and buffalo milk.

![Kiran Dairy](static/images/cow.jpg)

## ✨ Features

- 📊 **Milk Type Selection**: Choose between Cow Milk and Buffalo Milk
- 💰 **Dynamic Pricing**: Automatic price calculation based on fat content
- 👥 **Member Management**: Track multiple dairy members
- 📝 **Bill Generation**: Generate detailed bills with all information
- 🖨️ **Print Support**: Print bills directly from the browser
- 📱 **Responsive Design**: Works on desktop and mobile devices

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- **Python 3.7 or higher**
- **pip** (Python package installer)

## 🚀 Installation

### Step 1: Download the Application

Download and extract the `dairy_project` folder to your computer.

### Step 2: Install Python Dependencies

Open a terminal/command prompt in the `dairy_project` folder and run:

```bash
pip install -r requirements.txt
```

This will install:
- Flask (Web framework)
- Pillow (Image processing)
- Werkzeug (WSGI utilities)

### Step 3: Verify Data Files

Make sure the following files exist in the `data/` folder:
- `member_name.txt` - List of member names (one per line)
- `fat_price.txt` - Fat percentage and prices (format: `fat%,price`)

Example `member_name.txt`:
```
Rajesh Kumar
Priya Sharma
Amit Patel
```

Example `fat_price.txt`:
```
3.0,45
3.5,48
4.0,50
4.5,52
5.0,55
```

## 🎯 Running the Application

### Method 1: Using Python directly

```bash
python app.py
```

### Method 2: Using Flask command

```bash
flask run
```

The application will start on: **http://127.0.0.1:5000**

Open this URL in your web browser (Chrome, Firefox, Edge, etc.)

## 📖 How to Use

1. **Select Member**: Choose the dairy member from the dropdown
2. **Select Milk Type**: Choose Cow Milk or Buffalo Milk
3. **Select Fat Content**: Choose the fat percentage
4. **Enter Quantity**: Enter the quantity in liters
5. **Calculate Price**: Click the "Calculate Price" button
6. **View Bill**: The bill will be displayed with all details
7. **Print Bill**: Click "Print Bill" to print or save as PDF

## 📁 Project Structure

```
dairy_project/
│
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── README.md              # This file
│
├── data/
│   ├── member_name.txt    # Member names
│   └── fat_price.txt      # Fat prices
│
├── static/
│   ├── css/
│   │   ├── style.css      # Main stylesheet
│   │   └── image_update.css
│   └── images/
│       ├── cow.jpg        # Cow image
│       └── buffalo.jpg    # Buffalo image
│
└── templates/
    └── index.html         # Main HTML template
```

## ⚙️ Configuration

### Adding New Members

Edit `data/member_name.txt` and add member names (one per line):
```
New Member Name
Another Member
```

### Updating Prices

Edit `data/fat_price.txt` and update prices (format: `fat%,price`):
```
3.0,45
3.5,48
4.0,50
```

### Changing Port

To run on a different port, edit `app.py`:
```python
app.run(debug=True, port=8080)  # Change 5000 to 8080
```

## 🌐 Deployment Options

### Option 1: Local Network Access

To allow others on your local network to access:

1. Find your computer's IP address:
   - Windows: `ipconfig`
   - Linux/Mac: `ifconfig` or `ip addr`

2. Run the app with:
   ```bash
   python app.py
   ```
   Or modify `app.py`:
   ```python
   app.run(debug=False, host='0.0.0.0', port=5000)
   ```

3. Others can access at: `http://YOUR_IP_ADDRESS:5000`

### Option 2: Cloud Deployment

Deploy to platforms like:
- **Heroku** (Free tier available)
- **PythonAnywhere** (Free tier available)
- **Railway** (Free tier available)
- **Render** (Free tier available)

### Option 3: Share as ZIP

1. Compress the entire `dairy_project` folder
2. Share the ZIP file
3. Recipients follow the installation steps above

## 🛠️ Troubleshooting

### Port Already in Use
```bash
# Use a different port
python app.py --port 8080
```

### Module Not Found Error
```bash
# Reinstall dependencies
pip install -r requirements.txt
```

### Images Not Loading
- Check that `static/images/` folder contains `cow.jpg` and `buffalo.jpg`
- Clear browser cache (Ctrl+Shift+R)

### Data Files Not Found
- Ensure `data/member_name.txt` and `data/fat_price.txt` exist
- Check file paths are correct

## 📞 Support

For issues or questions, contact: **Kiran Dairy**

## 📄 License

This application is free to use for dairy management purposes.

---

**Made with ❤️ for Kiran Dairy**
