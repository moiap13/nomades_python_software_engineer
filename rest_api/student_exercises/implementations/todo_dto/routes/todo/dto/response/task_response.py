from marshmallow import Schema, fields

class TaskResponse(Schema):
  id = fields.UUID()
  task = fields.String()
  completed = fields.Boolean()
  created = fields.DateTime()