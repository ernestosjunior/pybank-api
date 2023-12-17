from datetime import datetime
from app import db


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    value = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    account_id = db.Column(db.Integer, db.ForeignKey("account.id"), nullable=False)
