from marshmallow import Schema, fields

from .user_response import UserResponse

class UserResponseList(Schema):
  users = fields.List(fields.Nested(UserResponse))