from flask import Flask, jsonify, request

app = Flask(__name__)

USERS = {1: {"id": 1, "name": "Alice", "role": "Admin"}}

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok", "service": "user-api"}), 200

@app.route("/api/v1/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = USERS.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user), 200

@app.route("/api/v1/users", methods=["POST"])
def create_user():
    data = request.get_json() or {}
    if "name" not in data:
        return jsonify({"error": "Missing required field: name"}), 400
    new_id = len(USERS) + 1
    new_user = {"id": new_id, "name": data["name"], "role": data.get("role", "User")}
    USERS[new_id] = new_user
    return jsonify(new_user), 201

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)