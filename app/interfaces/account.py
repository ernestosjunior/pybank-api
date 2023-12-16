from marshmallow import Schema, fields, validate
from app.models import AccountTypeEnum


class AccountSchema(Schema):
    id = fields.Integer()
    person_id = fields.Integer(required=True)
    balance = fields.Float()
    daily_withdrawal_limit = fields.Float()
    status = fields.Boolean()
    type = fields.Enum(AccountTypeEnum)
