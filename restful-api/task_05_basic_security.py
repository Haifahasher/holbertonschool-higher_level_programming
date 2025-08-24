#!/usr/bin/env python3
"""
Task 5: Flask API with SQLAlchemy (persistent storage)
"""

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure SQLite database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


# -------------------------
# Database Model
# -------------------------
class User(db.Model):
    """
    User model for storing user data
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=True)
    city = db.Column(db.String(120), nullable=True)

    def to_dict(self):
        """
        Convert model to dictionary
        """
        return {
            "id": self.id,
            "username": self.username,
            "age": self.age,
            "city": self.city
        }


# -------------------------
# Routes
# -------------------------
@app.route("/")
def home():
    return "Welcome to the Flask API with SQLAlchemy!"


@app.route("/data")
def data():
    """
    Return list of all usernames
    """
    users = User.query.all()
    return jsonify([user.username for user in users])


@app.route("/status")
def status():
    """
    Health check
    """
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """
    Get user details by username
    """
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user.to_dict())


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Add a new user
    """
    data = request.get_json()

    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    if User.query.filter_by(username=data["username"]).first():
        return jsonify({"error": "Username already exists"}), 400

    user = User(username=data["username"], age=data.get("age"), city=data.get("city"))
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User added", "user": user.to_dict()}), 201


# -------------------------
# Run App
# -------------------------
if __name__ == "__main__":
    # Create database tables
    with app.app_context():
        db.create_all()

    app.run(debug=True)

