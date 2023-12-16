from flask import jsonify, request
from app.interfaces.person import PersonSchema
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
from app.services.person import create_person_profile


def create_person():
    schema = PersonSchema()
    body = request.get_json()
    try:
        person = schema.load(body)
        person_created = create_person_profile(person)
        response_data = schema.dump(person_created)
        del response_data["password"]
        return response_data, 201

    except ValidationError as ve:
        return jsonify({"error": "Validation error.", "details": ve.messages}), 422

    except IntegrityError as ie:
        return jsonify({"error": "User already exists.", "details": str(ie)}), 409

    except Exception as e:
        return jsonify({"error": str(e)}), 400
