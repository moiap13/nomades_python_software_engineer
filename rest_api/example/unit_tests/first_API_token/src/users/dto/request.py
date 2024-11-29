from marshmallow import Schema, fields

class UserCreate(Schema):
  username = fields.String(required=True)
  firstname = fields.String(required=True)
  lastname = fields.String(required=True)
  password = fields.String(required=True)

class UpdateUser(Schema):
  username = fields.String()
  firstname = fields.String()
  lastname = fields.String()
  password = fields.String()