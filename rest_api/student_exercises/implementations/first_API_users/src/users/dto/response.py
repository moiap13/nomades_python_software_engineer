from marshmallow import Schema, fields

class UserResponse(Schema):
  id = fields.String()
  username = fields.String()

class UserDataResponse(UserResponse):
  firstname = fields.String()
  lastname = fields.String()

class UserDataResponseList(Schema):
  users = fields.List(fields.Nested(UserDataResponse))