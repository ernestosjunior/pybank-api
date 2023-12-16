from marshmallow import Schema, fields, validate
from app.models import AccountTypeEnum


class AccountSchema(Schema):
    id = fields.Integer()
    person_id = fields.Integer(required=True)
    status = fields.Boolean()
    type = fields.Enum(AccountTypeEnum)
