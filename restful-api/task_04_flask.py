#!/usr/bin/env python3
"""
Task 4: Develop a simple API using Flask
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory "database" for users
users = {}


@app.route("/")
def home():
    """
    Root endpoint
    """
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    """
    Return list of all usernames
    """
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """
    Health check endpoint
    """
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """
    Get user details by username
    """
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    return jsonify(users[username])


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Add a new user
    """
    user = request.get_json()

    if not user or "username" not in user:
        return jsonify({"error": "Username is required"}), 400

    users[user["username"]] = user
    return jsonify({"message": "User added", "user": user}), 201


if __name__ == "__main__":
    app.run(debug=True)

