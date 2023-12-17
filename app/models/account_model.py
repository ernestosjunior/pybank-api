from datetime import datetime
from app import db


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    balance = db.Column(db.Float, default=0)
    daily_withdrawal_limit = db.Column(db.Float, default=1000)
    status = db.Column(db.Boolean, default=True)
    type = db.Column(db.Integer, default=1)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    transactions = db.relationship("Transaction", backref="account", lazy=True)
    person_id = db.Column(
        db.Integer, db.ForeignKey("person.id"), unique=True, nullable=False
    )
