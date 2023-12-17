from flask import jsonify, request
from app.schemas.person import PersonSchema
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
from app.services.person import create_person_profile
from app.utils.http_status import (
    HTTP_STATUS_CREATED,
    HTTP_STATUS_VALIDATION_ERROR,
    HTTP_STATUS_CONFLICT,
    HTTP_STATUS_INTERNAL_SERVER_ERROR,
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
