from marshmallow import Schema, fields, validate


class LoginInput(Schema):
    email = fields.Str(required=True)
    password = fields.Str(required=True)
