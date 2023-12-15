from app import db

class Account(db.Model):
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    balance = db.Column(db.Float, default=0)
    daily_withdrawal_limit = db.Column(db.Float, default=1000)
    status = db.Column(db.Boolean, default=True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'), unique=True, nullable=False)
