from app import db


class Person(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.Text, nullable=False)
    cpf = db.Column(db.String(11), nullable=False, unique=True)
    birth_date = db.Column(db.Date, nullable=False)
    email = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {
            "name": self.name,
            "cpf": self.cpf,
            "birth_date": self.birth_date,
            "email": self.email
        }