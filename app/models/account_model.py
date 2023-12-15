from app import db
import enum
from datetime import datetime


class AccountTypeEnum(enum.Enum):
    CURRENT = "current"
    SAVINGS = "savings"


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    balance = db.Column(db.Float, default=0)
    daily_withdrawal_limit = db.Column(db.Float, default=1000)
    status = db.Column(db.Boolean, default=True)
    type = db.Column(db.Enum(AccountTypeEnum), default=AccountTypeEnum.CURRENT)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    person_id = db.Column(
        db.Integer, db.ForeignKey("person.id"), unique=True, nullable=False
    )
