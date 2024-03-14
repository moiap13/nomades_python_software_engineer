from marshmallow import Schema, fields

class UpdateBook(Schema):
  title = fields.String()
  summary = fields.String()