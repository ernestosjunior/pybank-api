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
        account = check_account(transaction.get("id"))

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
