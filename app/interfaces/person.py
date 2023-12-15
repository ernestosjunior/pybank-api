from marshmallow import Schema, fields, validate


class PersonInput(Schema):
    name = fields.Str(required=True)
    cpf = fields.Str(required=True, validate=validate.Length(equal=11))
    birth_date = fields.Date(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True)
