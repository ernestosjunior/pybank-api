from flask import jsonify

def create_transaction():
    return jsonify({"message": "CREATE TRANSACTION", "status": 201}),201