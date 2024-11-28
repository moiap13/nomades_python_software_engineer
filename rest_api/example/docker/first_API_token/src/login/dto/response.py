from marshmallow import Schema, fields

class LoginToken(Schema):
  token = fields.String()