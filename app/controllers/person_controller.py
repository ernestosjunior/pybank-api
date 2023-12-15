from flask import jsonify

def create_person():
    return jsonify({"message": "CREATE PERSON", "status": 201}),201