from marshmallow import Schema, fields

class LoginRequest(Schema):
  username_email = fields.String(required=True)
  password = fields.String(required=True)