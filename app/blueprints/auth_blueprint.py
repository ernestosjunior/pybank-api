from flask import Blueprint
from app.controllers import auth_controller

auth_blueprint = Blueprint("auth", __name__)

auth_blueprint.add_url_rule("/login", "login", auth_controller.login, methods=["POST"])
