from marshmallow import Schema, fields

class CreateTask(Schema):
  task = fields.String(required=True)
  completed = fields.Boolean(required=False)