from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity
from app.models import Person, Account
from app.interfaces.account import AccountInput
from app import db


def create_account():
    schema = AccountInput()
    body = request.get_json()
    try:
        account = schema.load(body)
        current_user = get_jwt_identity()
        person = Person.query.filter_by(email=current_user).first()

        if not person:
            return jsonify({"error": "User not found."}), 404

        account_created = Account(
            person_id=person.id, status=account.get("status"), type=account.get("type")
        )
        db.session.add(account_created)
        db.session.commit()
        response_data = schema.dump(account_created)
        return response_data, 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
