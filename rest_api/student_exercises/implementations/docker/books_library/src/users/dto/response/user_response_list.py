from marshmallow import Schema, fields
from .user_response import UserResponse, UserIdentifier

class UserResponseList(Schema):
  users = fields.List(fields.Nested(UserIdentifier))