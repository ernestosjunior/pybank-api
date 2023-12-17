from flask import Flask
from .auth_blueprint import auth_blueprint


def register_blueprints(app: Flask):
    app.register_blueprint(auth_blueprint)
