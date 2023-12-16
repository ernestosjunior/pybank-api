from marshmallow import Schema, fields, validate


class LoginSchema(Schema):
    email = fields.Str(required=True)
    password = fields.Str(required=True)
