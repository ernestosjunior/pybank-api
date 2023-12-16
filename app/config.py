from os import environ
from datetime import timedelta

SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
SQLALCHEMY_TRACK_MODIFICATIONS = environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")
JWT_SECRET_KEY = environ.get("JWT_SECRET_KEY")
JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=int(environ.get("JWT_ACCESS_TOKEN_EXPIRES")))
