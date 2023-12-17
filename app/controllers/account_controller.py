from flask import jsonify, request
from marshmallow import ValidationError
from app.exceptions import NotFoundException, NotAllowedException
from app.schemas.account import AccountSchema
from app.services.account import (
    create_account_for_person,
    check_account,
    update_account_status,
)
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
                    "error": "An error occurred.",
                    "details": str(e),
                }
            ),
            500,
        )


def get_balance(account_id):
    try:
        account = check_account(account_id)
        return jsonify({"balance": account.balance}), 200
    except Exception as e:
        return (
            jsonify(
                {
                    "error": "An error occurred.",
                    "details": str(e),
                }
            ),
            500,
        )


def block_account(account_id: int):
    schema = AccountSchema()
    try:
        account = check_account(account_id)
        update_account_status(account, False)
        return schema.dump(account), 200
    except Exception as e:
        return (
            jsonify(
                {
                    "error": "An error occurred.",
                    "details": str(e),
                }
            ),
            500,
        )
