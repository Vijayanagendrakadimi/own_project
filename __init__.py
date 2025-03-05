# filepath: /my-python-project/my-python-project/app/__init__.py
from flask import Flask

app = Flask(__name__)

# Configuration settings can be added here
app.config['SECRET_KEY'] = 'your_secret_key'

from app import main  # Import the main module to register routes