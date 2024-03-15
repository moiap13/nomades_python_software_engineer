from marshmallow import Schema, fields

class BorrowResponse(Schema):
  book_isbn = fields.Str()
  start = fields.DateTime()
  end = fields.DateTime()