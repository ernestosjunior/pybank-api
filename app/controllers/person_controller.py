from flask import jsonify, request
from app.schemas.person import PersonSchema
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
from app.services.person import create_person_profile
from flask_jwt_extended import get_jwt_identity
from app.exceptions import NotFoundException
from app.services.auth import check_person
from app.utils.http_status import (
    HTTP_STATUS_CREATED,
    HTTP_STATUS_VALIDATION_ERROR,
    HTTP_STATUS_CONFLICT,
    HTTP_STATUS_INTERNAL_SERVER_ERROR,
    HTTP_STATUS_NOT_FOUND,
)


def create_person():
    schema = PersonSchema()
    body = request.get_json()
    try:
        person = schema.load(body)
        person_created = create_person_profile(person)
        response_data = schema.dump(person_created)
        del response_data["password"]
        return response_data, HTTP_STATUS_CREATED

    except ValidationError as ve:
        return (
            jsonify({"error": "Validation error.", "details": ve.messages}),
            HTTP_STATUS_VALIDATION_ERROR,
        )

    except IntegrityError as ie:
        return (
            jsonify({"error": "User already exists.", "details": str(ie)}),
            HTTP_STATUS_CONFLICT,
        )

    except Exception as e:
        return (
            jsonify(
                {
                    "error": "An error occurred.",
                    "details": str(e),
                }
            ),
            HTTP_STATUS_INTERNAL_SERVER_ERROR,
        )


def get_person():
    schema = PersonSchema()
    id = get_jwt_identity()
    try:
        person = check_person(id)
        response = schema.dump(person)
        del response["password"]
        return response, 200
    except NotFoundException as nfe:
        return jsonify({"error": nfe.message}), HTTP_STATUS_NOT_FOUND
    except Exception as e:
        return (
            jsonify(
                {
                    "error": "An error occurred.",
                    "details": str(e),
                }
            ),
            HTTP_STATUS_INTERNAL_SERVER_ERROR,
        )
