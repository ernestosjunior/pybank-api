from app import db
from datetime import datetime
import enum


class TransactionTypeEnum(enum.Enum):
    CREDIT = "credit"
    DEBIT = "debit"


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    value = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    type = db.Column(db.Enum(TransactionTypeEnum), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey("account.id"), nullable=False)
