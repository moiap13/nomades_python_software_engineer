from marshmallow import Schema, fields

class LoginRequest(Schema):
  username = fields.String(required=True)
  password = fields.String(required=True)