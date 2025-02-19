from marshmallow import Schema, fields

class CreateBook(Schema):
  title = fields.String(required=True)
  authors = fields.List(fields.String)
  isbn = fields.String()
