from flask_bcrypt import Bcrypt
from app import app

bcrypt = Bcrypt(app)


def generate_hash(password: str) -> str():
    return bcrypt.generate_password_hash(password).decode("utf-8")


def check_hash(hash: str, password: str) -> bool:
    return bcrypt.check_password_hash(pw_hash=hash, password=password)
