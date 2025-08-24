#!/usr/bin/env python3
"""
Task 5: Flask API with Basic Authentication
"""

from flask import Flask, jsonify
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

# Hardcoded users for demo (username: password)
users = {
    "admin": "secret",
    "john": "hello"
}

@auth.verify_password
def verify_password(username, password):
    if username in users and users[username] == password:
        return username
    return None


@app.route("/")
def home():
    return "Welcome to the secure Flask API!"


@app.route("/status")
def status():
    return "OK"


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """
    A protected endpoint requiring Basic Auth
    """
    return jsonify({"message": f"Hello, {auth.current_user()}! You are authenticated."})


if __name__ == "__main__":
    app.run(debug=True)
