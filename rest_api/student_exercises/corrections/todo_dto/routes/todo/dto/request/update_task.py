from marshmallow import Schema, fields

class UpdateTask(Schema):
  task = fields.String()
  completed = fields.Boolean()