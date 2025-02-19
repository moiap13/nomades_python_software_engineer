from marshmallow import Schema, fields

class BorrowRequest(Schema):
  book_id = fields.String(required=True)
  start = fields.DateTime(required=True)
  end = fields.DateTime(required=True)