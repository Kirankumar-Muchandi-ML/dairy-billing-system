from flask import Flask, render_template, request, jsonify
import os
from datetime import datetime

app = Flask(__name__)

# Read member names from file
def get_members():
    members = []
    with open('data/member_name.txt', 'r') as f:
        members = [line.strip() for line in f.readlines() if line.strip()]
    return members

# Read fat prices from file
def get_fat_prices():
    fat_prices = {}
    with open('data/fat_price.txt', 'r') as f:
        for line in f:
            if line.strip():
                fat, price = line.strip().split(',')
                fat_prices[float(fat)] = float(price)
    return fat_prices

# Calculate milk price
def calculate_price(liters, fat_content, milk_type):
    fat_prices = get_fat_prices()
    
    # Get base price for fat content
    base_price = fat_prices.get(float(fat_content), 0)
    
    # Buffalo milk is typically 10% more expensive
    if milk_type == 'Buffalo':
        base_price = base_price * 1.1
    
    # Calculate total price
    total_price = base_price * float(liters)
    
    return round(total_price, 2)

@app.route('/')
def index():
    members = get_members()
    fat_prices = get_fat_prices()
    fat_options = sorted(fat_prices.keys())
    return render_template('index.html', members=members, fat_options=fat_options)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    
    member_name = data.get('member_name')
    liters = float(data.get('liters'))
    fat_content = float(data.get('fat_content'))
    milk_type = data.get('milk_type')
    
    total_price = calculate_price(liters, fat_content, milk_type)
    
    result = {
        'member_name': member_name,
        'liters': liters,
        'fat_content': fat_content,
        'milk_type': milk_type,
        'total_price': total_price,
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    return jsonify(result)

@app.route('/print_receipt', methods=['POST'])
def print_receipt():
    data = request.json
    
    # Create receipt text
    receipt = f"""
{'='*40}
        KIRAN DAIRY
{'='*40}
Date: {data['date']}
Member: {data['member_name']}
Milk Type: {data['milk_type']}
Fat Content: {data['fat_content']}%
Quantity: {data['liters']} Liters
{'='*40}
Total Price: Rs. {data['total_price']}/-
{'='*40}
    Thank you for your business!
{'='*40}
"""
    
    # Save receipt to file (for printing)
    receipt_file = f"receipts/receipt_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    os.makedirs('receipts', exist_ok=True)
    
    with open(receipt_file, 'w') as f:
        f.write(receipt)
    
    # For actual printing, you would use a library like python-escpos
    # or send the file to the printer using system commands
    # Example: os.system(f'lpr {receipt_file}')  # Linux/Mac
    # Example: os.system(f'print {receipt_file}')  # Windows
    
    return jsonify({'status': 'success', 'message': 'Receipt saved', 'file': receipt_file})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
