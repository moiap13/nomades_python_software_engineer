from marshmallow import Schema, fields

class UserResponse(Schema):
  id = fields.String()
  firstname = fields.String()
  lastname = fields.String()
  username = fields.String()
  email = fields.String()
  password = fields.String()
  salt = fields.String()

class UserIdentifier(Schema):
  id = fields.String()
  username = fields.String()
  email = fields.String() 

class UserData(UserIdentifier):
  firstname = fields.String()
  lastname = fields.String()