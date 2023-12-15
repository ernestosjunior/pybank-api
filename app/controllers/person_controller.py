from flask import jsonify, request

def create_person():
    person = request.get_json()
    return jsonify(person), 201
