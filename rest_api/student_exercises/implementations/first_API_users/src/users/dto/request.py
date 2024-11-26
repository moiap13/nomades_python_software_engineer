from marshmallow import Schema, fields

class UserCreate(Schema):
  username = fields.String(required=True)
  firstname = fields.String(required=True)
  lastname = fields.String(required=True)
  password = fields.String(required=True)

class UpdateUser(Schema):
  # TODO: add the acceptable update fields
  pass