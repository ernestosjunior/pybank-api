from flask import jsonify


def create_account():
    return jsonify({"message": "CREATE ACCOUNT", "status": 201}), 201
