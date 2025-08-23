from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    return jsonify([username for username in users.keys()])


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>")
def get_users(username):
    if username not in users:
        return {"error": "User not found"}, 404
    return jsonify(users[username])


@app.route("/add_user", methods=["POST"])
def add_user():
    user = request.get_json()
    if "username" not in user.keys():
        return {"error": "Username is required"}, 400
    users[user["username"]] = user
    return {"message": "User added", "user": user}, 201


if __name__ == "__main__":
    app.run()
