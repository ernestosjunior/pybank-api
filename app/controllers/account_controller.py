from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity
from marshmallow import ValidationError
from app.models import Person
from app.interfaces.account import AccountInput
from app.services.account import create_account_for_person
from sqlalchemy.exc import IntegrityError


def create_account():
    schema = AccountInput()
    body = request.get_json()
    try:
        account = schema.load(body)
        current_user = get_jwt_identity()
        person = Person.query.filter_by(email=current_user).first()

        if not person:
            return jsonify({"error": "User not found."}), 404

        account_created = create_account_for_person(person.id, account)
        response_data = schema.dump(account_created)
        return response_data, 201

    except ValidationError as ve:
        return jsonify({"error": ve.messages}), 422

    except IntegrityError as ie:
        return jsonify({"error": "User already exists.", "details": str(ie)}), 409

    except Exception as e:
        return (
            jsonify(
                {
                    "error": "An error occurred while creating the account.",
                    "details": str(e),
                }
            ),
            500,
        )
