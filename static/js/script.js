// Store current bill data
let currentBill = null;

// Form submission handler
document.getElementById('billingForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const formData = {
        member_name: document.getElementById('member_name').value,
        milk_type: document.getElementById('milk_type').value,
        fat_content: document.getElementById('fat_content').value,
        liters: document.getElementById('liters').value
    };
    
    try {
        const response = await fetch('/calculate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });
        
        const result = await response.json();
        currentBill = result;
        
        // Display results
        document.getElementById('res_member').textContent = result.member_name;
        document.getElementById('res_type').textContent = result.milk_type;
        document.getElementById('res_fat').textContent = result.fat_content;
        document.getElementById('res_liters').textContent = result.liters;
        document.getElementById('res_price').textContent = result.total_price;
        
        // Show result section
        document.getElementById('result').classList.remove('hidden');
        
        // Scroll to result
        document.getElementById('result').scrollIntoView({ behavior: 'smooth' });
        
    } catch (error) {
        alert('Error calculating price. Please try again.');
        console.error('Error:', error);
    }
});

// Print receipt handler
document.getElementById('printBtn').addEventListener('click', async function() {
    if (!currentBill) {
        alert('No bill data available');
        return;
    }
    
    try {
        const response = await fetch('/print_receipt', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(currentBill)
        });
        
        const result = await response.json();
        
        if (result.status === 'success') {
            alert('Receipt saved successfully!\nFile: ' + result.file + '\n\nNote: To print, configure your printer and update the print command in app.py');
            
            // Reset form
            document.getElementById('billingForm').reset();
            document.getElementById('result').classList.add('hidden');
            currentBill = null;
        }
        
    } catch (error) {
        alert('Error printing receipt. Please try again.');
        console.error('Error:', error);
    }
});

// Highlight selected milk type
document.getElementById('milk_type').addEventListener('change', function() {
    const cowImg = document.getElementById('cow-img');
    const buffaloImg = document.getElementById('buffalo-img');
    
    if (this.value === 'Cow') {
        cowImg.style.border = '5px solid #4CAF50';
        buffaloImg.style.border = 'none';
    } else if (this.value === 'Buffalo') {
        buffaloImg.style.border = '5px solid #4CAF50';
        cowImg.style.border = 'none';
    } else {
        cowImg.style.border = 'none';
        buffaloImg.style.border = 'none';
    }
});
