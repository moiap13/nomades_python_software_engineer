import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

from marshmallow import Schema, fields

from books.dto.response.book_response import BookResponse
from users.dto.response.user_response import UserData

class BorrowResponse(Schema):
  id = fields.String()
  book = fields.Nested(BookResponse)
  user = fields.Nested(UserData)
  start = fields.DateTime()
  end = fields.DateTime()