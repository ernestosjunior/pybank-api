from flask import jsonify, request
from flask_jwt_extended import create_access_token
from app.schemas.auth import LoginSchema
from app.utils.hash import check_hash
from app.models import Person


def login():
    schema = LoginSchema()
    body = request.get_json()
    try:
        login_data = schema.load(body)
        person = Person.query.filter_by(email=login_data.get("email")).first()

        if person:
            is_valid_password = check_hash(person.password, login_data.get("password"))

            if is_valid_password:
                access_token = create_access_token(identity=person.id)
                return (
                    jsonify(
                        id=person.id,
                        email=person.email,
                        name=person.name,
                        access_token=access_token,
                    ),
                    201,
                )
            else:
                return jsonify({"error": "Invalid credentials."}), 401
        else:
            return jsonify({"error": "User not found."}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 400
