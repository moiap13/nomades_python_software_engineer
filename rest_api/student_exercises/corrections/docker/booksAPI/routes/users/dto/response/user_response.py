from marshmallow import Schema, fields

class UserResponse(Schema):
    id = fields.String()
    name = fields.String()
    email = fields.String()