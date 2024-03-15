from marshmallow import Schema, fields

class UserCreateRequest(Schema):
  name = fields.String(required=True)
  email = fields.String(required=True)
  password = fields.String(required=True)