from flask import jsonify, request
from app.schemas.transaction import TransactionSchema
from app.services.transaction import add_transaction
from app.services.account import update_account_balance, check_account
from app.exc import NotFoundException, NotAllowedException
from marshmallow import ValidationError


def create_transaction():
    schema = TransactionSchema()
    body = request.get_json()
    try:
        transaction = schema.load(body)
        account = check_account(transaction.get("account_id"))

        value = transaction.get("value")
        valid_daily_limit = value <= 0 and abs(value) <= account.daily_withdrawal_limit

        if not valid_daily_limit:
            return jsonify({"error": "Amount exceeds daily withdrawal limit."}), 400

        created_transaction = add_transaction(transaction)
        update_account_balance(account, transaction)

        schema.dump(created_transaction)
        return schema.dump(created_transaction), 201

    except NotFoundException as nfe:
        return jsonify({"error": nfe.message}), 404

    except NotAllowedException as nae:
        return jsonify({"error": nae.message}), 403

    except ValidationError as ve:
        return jsonify({"error": "Validation error.", "details": ve.messages}), 422

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
