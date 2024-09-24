from marshmallow import Schema, fields

class CreateUserRequest(Schema):
  firstname = fields.String(required=True)
  lastname = fields.String(required=True)
  username = fields.String(required=True)
  password = fields.String(required=True)
  email = fields.String(required=True, validate=lambda x: "@" in x)

