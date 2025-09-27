#!/usr/bin/env python3
"""
Flask application that displays product data from JSON or CSV files.
Supports filtering by product ID and handles various error cases.
"""

import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)


def load_json_data():
    """Load product data from JSON file."""
    try:
        with open('products.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def load_csv_data():
    """Load product data from CSV file."""
    products = []
    try:
        with open('products.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert string values to appropriate types
                product = {
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                }
                products.append(product)
    except (FileNotFoundError, KeyError, ValueError):
        return []
    return products


def filter_products(products, product_id):
    """Filter products by ID."""
    if product_id is None:
        return products
    
    try:
        product_id = int(product_id)
        filtered = [p for p in products if p['id'] == product_id]
        return filtered
    except ValueError:
        return []


@app.route('/products')
def products():
    """Products page route with dynamic content from JSON or CSV."""
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id')
    
    products_data = []
    error_message = None
    
    if source == 'json':
        products_data = load_json_data()
    elif source == 'csv':
        products_data = load_csv_data()
    else:
        error_message = "Wrong source"
        return render_template('product_display.html', 
                             products=[], 
                             error_message=error_message)
    
    # Filter by ID if provided
    if product_id:
        products_data = filter_products(products_data, product_id)
        if not products_data:
            error_message = "Product not found"
    
    return render_template('product_display.html', 
                         products=products_data, 
                         error_message=error_message)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
