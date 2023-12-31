from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity
from marshmallow import ValidationError
from app.exceptions import NotFoundException, NotAllowedException
from app.schemas.account import AccountSchema
from app.schemas.transaction import TransactionSchema
from app.services.account import (
    create_account_for_person,
    check_account,
    update_account_status,
    get_account_by_person_id,
)
from sqlalchemy.exc import IntegrityError
from app.services.auth import check_person
from app.utils.http_status import (
    HTTP_STATUS_CREATED,
    HTTP_STATUS_NOT_FOUND,
    HTTP_STATUS_NOT_ALLOWED,
    HTTP_STATUS_OK,
    HTTP_STATUS_VALIDATION_ERROR,
    HTTP_STATUS_CONFLICT,
    HTTP_STATUS_INTERNAL_SERVER_ERROR,
)


def create_account():
    schema = AccountSchema()
    body = request.get_json()
    try:
        account = schema.load(body)
        person = check_person(account.get("person_id"))

        account_created = create_account_for_person(person.id, account)
        response_data = schema.dump(account_created)
        return response_data, HTTP_STATUS_CREATED

    except NotFoundException as nfe:
        return jsonify({"error": nfe.message}), HTTP_STATUS_NOT_FOUND

    except NotAllowedException as nae:
        return jsonify({"error": nae.message}), HTTP_STATUS_NOT_ALLOWED

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


def get_balance(account_id):
    try:
        account = check_account(account_id)
        return jsonify({"balance": account.balance}), HTTP_STATUS_OK
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


def block_account(account_id: int):
    schema = AccountSchema()
    try:
        account = check_account(account_id)
        update_account_status(account, False)
        return schema.dump(account), HTTP_STATUS_OK
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


def get_account():
    schema = AccountSchema()
    schema_transaction = TransactionSchema()
    try:
        person_id = get_jwt_identity()
        account = get_account_by_person_id(person_id)

        account_data = schema.dump(account)
        account_data["transactions"] = [
            schema_transaction.dump(t) for t in account.transactions
        ]

        return account_data, 200

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
