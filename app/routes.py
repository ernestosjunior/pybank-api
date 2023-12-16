from app import app
from app.controllers import person_controller
from app.controllers import auth_controller
from app.controllers import account_controller
from app.controllers import transaction_controller
from flask_jwt_extended import jwt_required


app.add_url_rule("/login", "login", auth_controller.login, methods=["POST"])

app.add_url_rule(
    "/person",
    "create_person",
    person_controller.create_person,
    methods=["POST"],
)

# Authenticated routes
app.add_url_rule(
    "/account",
    "create_account",
    jwt_required()(account_controller.create_account),
    methods=["POST"],
)

app.add_url_rule(
    "/transaction/credit",
    "create__debit_transaction",
    jwt_required()(transaction_controller.create__debit_transaction),
    methods=["POST"],
)
