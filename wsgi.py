"""
WSGI configuration for Kiran Dairy Billing System
For PythonAnywhere deployment
"""

import sys
import os

# Add your project directory to the sys.path
project_home = '/home/YOUR_USERNAME/dairy-billing-system'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Import the Flask app
from app import app as application

# This is required for PythonAnywhere
if __name__ == "__main__":
    application.run()
