from app import db

class Person(db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.Text, nullable=False)