from marshmallow import Schema, fields

class BookResponse(Schema):
  isbn = fields.String()
  title = fields.String()
  summary = fields.String()