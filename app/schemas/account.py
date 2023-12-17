from marshmallow import Schema, fields
from app.models import AccountType


class AccountSchema(Schema):
    id = fields.Integer()
    person_id = fields.Integer(required=True)
    balance = fields.Float()
    daily_withdrawal_limit = fields.Float()
    status = fields.Boolean()
    type = fields.Enum(AccountType, required=True)
