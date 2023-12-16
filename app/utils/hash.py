from flask_bcrypt import Bcrypt
from app import app


def generate_hash(password: str) -> str():
    bcrypt = Bcrypt(app)
    return bcrypt.generate_password_hash(password).decode("utf-8")


def check_hash(hash: str, password: str) -> bool:
    bcrypt = Bcrypt(app)
    return bcrypt.check_password_hash(pw_hash=hash, password=password)
