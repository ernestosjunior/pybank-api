from marshmallow import Schema, fields


class TransactionSchema(Schema):
    id = fields.Integer()
    value = fields.Float(required=True)
    created_at = fields.DateTime()
    account_id = fields.Integer(required=True)
