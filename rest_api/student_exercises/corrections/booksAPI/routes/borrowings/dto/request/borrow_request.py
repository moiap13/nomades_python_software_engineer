from marshmallow import Schema, fields

class BorrowRequest(Schema):
  book_isbn = fields.Str(required=True)
  nb_days = fields.Int(required=True)