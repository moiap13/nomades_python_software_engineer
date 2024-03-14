from marshmallow import Schema, fields

class LoginRequest(Schema):
    email = fields.String(required=True)
    password = fields.String(required=True)