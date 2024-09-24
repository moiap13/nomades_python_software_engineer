from marshmallow import Schema, fields

class UserResponse(Schema):
  id = fields.String()
  firstname = fields.String()
  lastname = fields.String()
  username = fields.String()
  password = fields.String()
  salt = fields.String()

class UserId(Schema):
  id = fields.String()

class UserResponseWithMessage(Schema):
  message = fields.String()
  data = fields.Nested(UserResponse)