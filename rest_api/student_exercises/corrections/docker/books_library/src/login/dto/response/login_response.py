from marshmallow import Schema, fields

class LoginResponse(Schema):
  token = fields.String()