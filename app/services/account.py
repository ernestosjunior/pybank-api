from app.models import Account
from app import db


def create_account_for_person(person_id: str, account_data):
    account_created = Account(
        person_id=person_id,
        status=account_data.get("status"),
        type=account_data.get("type"),
    )
    db.session.add(account_created)
    db.session.commit()
    return account_created


def update_account_balance(account, transaction):
    account.balance += float(transaction.get("value"))
    db.session.commit()
