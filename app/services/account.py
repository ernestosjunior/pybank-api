from app.models import Account
from app import db
from flask_jwt_extended import get_jwt_identity
from app.exc import NotFoundException, NotAllowedException
from app.schemas.account import AccountSchema
from app.schemas.transaction import TransactionSchema


def create_account_for_person(person_id: str, account_data: AccountSchema) -> Account:
    account_created = Account(
        person_id=person_id,
        status=account_data.get("status"),
        type=account_data.get("type"),
    )
    db.session.add(account_created)
    db.session.commit()
    return account_created


def update_account_balance(account: Account, transaction: TransactionSchema):
    account.balance += float(transaction.get("value"))
    db.session.commit()


def check_account(current_account: int) -> Account:
    current_user_id = get_jwt_identity()
    account = Account.query.filter_by(person_id=current_user_id).first()

    if not account:
        raise NotFoundException("Account not found.")

    is_current_account = account.id == current_account

    if not is_current_account:
        raise NotAllowedException(
            "It is not possible to create an transaction for another account."
        )

    return account


def update_account_status(account: Account, status: bool):
    account.status = status
    db.session.commit()
