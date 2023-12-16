from flask import jsonify, request
from app.schemas.transaction import TransactionSchema
from app.services.auth import check_account
from app.services.transaction import add_transaction
from app.exc import NotFoundException, NotAllowedException
from marshmallow import ValidationError


def create__debit_transaction():
    schema = TransactionSchema()
    body = request.get_json()
    try:
        transaction = schema.load(body)
        account = check_account(transaction)

        has_balance = account.balance >= transaction.get("value")

        if not has_balance:
            return (
                jsonify({"error": "Account does not have balance for transaction."}),
                403,
            )

        created_transaction = add_transaction(transaction)
        schema.dump(created_transaction)
        return schema.dump(created_transaction), 201

    except NotFoundException as nfe:
        return jsonify({"error": nfe.message}), 404

    except NotAllowedException as nae:
        return jsonify({"error": nae.message}), 403

    except ValidationError as ve:
        return jsonify({"error": "Validation error.", "details": ve.messages}), 422

    except Exception as e:
        return jsonify({"error": str(e)}), 400
