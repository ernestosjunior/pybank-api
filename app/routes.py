from flask import Flask
from flask_jwt_extended import jwt_required
from app.controllers import auth_controller
from app.controllers import person_controller
from app.controllers import account_controller
from app.controllers import transaction_controller


def register_routes(app: Flask):
    app.add_url_rule("/login", "login", auth_controller.login, methods=["POST"])

    app.add_url_rule(
        "/persons",
        "create_person",
        person_controller.create_person,
        methods=["POST"],
    )

    # Authenticated routes

    app.add_url_rule(
        "/person",
        "get_person",
        jwt_required()(person_controller.get_person),
        methods=["GET"],
    )

    app.add_url_rule(
        "/accounts",
        "create_account",
        jwt_required()(account_controller.create_account),
        methods=["POST"],
    )

    app.add_url_rule(
        "/account",
        "get_account",
        jwt_required()(account_controller.get_account),
        methods=["GET"],
    )

    app.add_url_rule(
        "/transactions",
        "create_transaction",
        jwt_required()(transaction_controller.create_transaction),
        methods=["POST"],
    )

    app.add_url_rule(
        "/transactions/<int:account_id>",
        "get_all_by_account_id",
        jwt_required()(transaction_controller.get_all_by_account_id),
        methods=["GET"],
    )

    app.add_url_rule(
        "/accounts/balance/<int:account_id>",
        "get_balance",
        jwt_required()(account_controller.get_balance),
        methods=["GET"],
    )

    app.add_url_rule(
        "/accounts/block/<int:account_id>",
        "block_account",
        jwt_required()(account_controller.block_account),
        methods=["PATCH"],
    )
