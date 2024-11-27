from marshmallow import Schema, fields

class LoginUser(Schema):
  username = fields.String(required=True)
  password = fields.String(required=True)