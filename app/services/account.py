from app.models import Account
from app import db


def create_account_for_person(person_id, account_data):
    account_created = Account(
        person_id=person_id,
        status=account_data.get("status"),
        type=account_data.get("type"),
    )
    db.session.add(account_created)
    db.session.commit()
    return account_created
