from marshmallow import Schema, fields

class CreateBook(Schema):
  isbn = fields.String(required=True)
  title = fields.String(required=True)
  summary = fields.String(required=True)