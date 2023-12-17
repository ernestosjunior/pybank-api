from flask import Flask
from dotenv import load_dotenv
from .extensions import db, migrate, jwt


def create_app():
    app = Flask(__name__)

    load_dotenv()

    app.config.from_pyfile("config.py")

    jwt.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    return app


from app.models import *
