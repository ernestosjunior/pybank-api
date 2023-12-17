from marshmallow import Schema, fields


class AccountSchema(Schema):
    id = fields.Integer()
    person_id = fields.Integer(required=True)
    balance = fields.Float()
    daily_withdrawal_limit = fields.Float()
    status = fields.Boolean()
    type = fields.Integer(required=True)
