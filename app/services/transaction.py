from app import db
from app.models import Transaction


def add_transaction(transaction_data) -> Transaction:
    transaction_created = Transaction(
        value=transaction_data.get("value"),
        account_id=transaction_data.get("account_id"),
    )
    db.session.add(transaction_created)
    db.session.commit()
    return transaction_created
