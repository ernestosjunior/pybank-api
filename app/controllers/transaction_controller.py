from flask import jsonify, request
from app.schemas.transaction import TransactionSchema
from app.services.transaction import add_transaction, get_all_transactions_by_account_id
from app.services.account import update_account_balance, check_account
from app.exceptions import NotFoundException, NotAllowedException
from marshmallow import ValidationError
from app.utils.http_status import (
    HTTP_STATUS_BAD_REQUEST,
    HTTP_STATUS_CREATED,
    HTTP_STATUS_NOT_FOUND,
    HTTP_STATUS_NOT_ALLOWED,
    HTTP_STATUS_VALIDATION_ERROR,
    HTTP_STATUS_INTERNAL_SERVER_ERROR,
    HTTP_STATUS_OK,
)


def create_transaction():
    schema = TransactionSchema()
    body = request.get_json()
    try:
        transaction = schema.load(body)
        account = check_account(transaction.get("account_id"))

        value = transaction.get("value")
        valid_daily_limit = value <= 0 and abs(value) <= account.daily_withdrawal_limit

        if not valid_daily_limit:
            return (
                jsonify({"error": "Amount exceeds daily withdrawal limit."}),
                HTTP_STATUS_NOT_ALLOWED,
            )

        created_transaction = add_transaction(transaction)
        update_account_balance(account, transaction)

        schema.dump(created_transaction)
        return schema.dump(created_transaction), HTTP_STATUS_CREATED

    except NotFoundException as nfe:
        return jsonify({"error": nfe.message}), HTTP_STATUS_NOT_FOUND

    except NotAllowedException as nae:
        return jsonify({"error": nae.message}), HTTP_STATUS_NOT_ALLOWED

    except ValidationError as ve:
        return (
            jsonify({"error": "Validation error.", "details": ve.messages}),
            HTTP_STATUS_VALIDATION_ERROR,
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


def get_all_by_account_id(account_id: int):
    try:
        transactions = get_all_transactions_by_account_id(account_id)
        return jsonify(transactions), HTTP_STATUS_OK
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
