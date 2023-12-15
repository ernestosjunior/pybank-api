from app import db


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.Text, nullable=False)
    cpf = db.Column(db.String(11), nullable=False, unique=True)
    birth_date = db.Column(db.Date, nullable=False)
    email = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)

    account = db.relationship("Account", uselist=False, backref="person", lazy=True)
