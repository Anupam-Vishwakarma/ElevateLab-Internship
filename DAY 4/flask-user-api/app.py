from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user storage (dictionary)
users = {}

# Home route
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to User Management API"}), 200


# GET all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200


# GET single user by ID
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404


# CREATE user
@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "Invalid input"}), 400

    user_id = len(users) + 1
    users[user_id] = {"id": user_id, "name": data["name"], "email": data["email"]}
    return jsonify(users[user_id]), 201


# UPDATE user
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.json
    user = users.get(user_id)

    if not user:
        return jsonify({"error": "User not found"}), 404

    user["name"] = data.get("name", user["name"])
    user["email"] = data.get("email", user["email"])
    return jsonify(user), 200


# DELETE user
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id in users:
        deleted_user = users.pop(user_id)
        return jsonify({"message": "User deleted", "user": deleted_user}), 200
    return jsonify({"error": "User not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
