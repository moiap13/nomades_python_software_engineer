from marshmallow import Schema, fields
from .task_response import TaskResponse

class ListTaskResponse(Schema):
  tasks = fields.List(fields.Nested(TaskResponse))