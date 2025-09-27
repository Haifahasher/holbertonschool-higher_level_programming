#!/usr/bin/env python3
"""
Flask application with dynamic templates using Jinja loops and conditions.
Reads data from JSON files and displays it dynamically.
"""

import json
from flask import Flask, render_template

app = Flask(__name__)


def load_items():
    """Load items from JSON file."""
    try:
        with open('items.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data.get('items', [])
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


@app.route('/')
def home():
    """Home page route."""
    return render_template('index.html')


@app.route('/about')
def about():
    """About page route."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Contact page route."""
    return render_template('contact.html')


@app.route('/items')
def items():
    """Items page route with dynamic content."""
    items_list = load_items()
    return render_template('items.html', items=items_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
