from flask import jsonify, request
from marshmallow import ValidationError
from app.exc import NotFoundException, NotAllowedException
from app.schemas.account import AccountSchema
from app.services.account import create_account_for_person
from sqlalchemy.exc import IntegrityError
from app.services.auth import check_person


def create_account():
    schema = AccountSchema()
    body = request.get_json()
    try:
        account = schema.load(body)
        person = check_person(account)

        account_created = create_account_for_person(person.id, account)
        response_data = schema.dump(account_created)
        return response_data, 201

    except NotFoundException as nfe:
        return jsonify({"error": nfe.message}), 404

    except NotAllowedException as nae:
        return jsonify({"error": nae.message}), 403

    except ValidationError as ve:
        return jsonify({"error": "Validation error.", "details": ve.messages}), 422

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
