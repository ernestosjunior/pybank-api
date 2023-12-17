from typing import List
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


def get_all_transactions_by_account_id(account_id) -> List[Transaction]:
    transactions = Transaction.query.filter_by(account_id=account_id)
    transactions_json = [
        {
            "id": transaction.id,
            "value": transaction.value,
            "created_at": str(transaction.created_at),
            "account_id": transaction.account_id,
        }
        for transaction in transactions
    ]
    return transactions_json
