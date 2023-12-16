from marshmallow import Schema, fields, validate
from app.models import AccountTypeEnum


class AccountInput(Schema):
    person_id = fields.Integer(required=True)
    status = fields.Boolean()
    type = fields.Enum(AccountTypeEnum)
