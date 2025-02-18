from marshmallow import Schema, fields

class BookResponse(Schema):
  id = fields.String()
  title = fields.String()
  authors = fields.List(fields.String)
  isbn = fields.String()
