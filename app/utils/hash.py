from flask_bcrypt import Bcrypt
from app import app


def generate_hash(password: str) -> str():
    bcrypt = Bcrypt(app)
    return bcrypt.generate_password_hash(password).decode("utf-8")
