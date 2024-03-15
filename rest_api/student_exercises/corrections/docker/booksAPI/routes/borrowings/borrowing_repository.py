import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

from config.database import db

from datetime import datetime

from .borrowing import Borrowing
from .borrowing_mapper import toEntity

class BorrowingRepository():
  def __init__(self) -> None:
    self.users_collection = db.collection(u"users")
    self.books_collection = db.collection(u"books")

  def borrows(self, user_id: str, book_isbn: str, delta_time) -> Borrowing:
    book = self.books_collection.document(book_isbn)
    book_free = book.get().to_dict().get("free", False)

    if not book_free:
      raise Exception("Book already borrowed")

    assert book_free

    start = datetime.now()
    end = start + delta_time
    borrow = {
      u"start": start,
      u"end": end,
      u"book_isbn": book_isbn
    }
    user_ref = self.users_collection.document(user_id)

    borrowed_books: list = user_ref.get().to_dict().get("borrowed_books", [])
    borrowed_books.append(borrow)
    # borrowed_books = sorted(borrowed_books, key=lambda x: x["start"], reverse=True)
    user_ref.update({u"borrowed_books": borrowed_books})

    book.update({u"free": False})
    return toEntity(borrow)
  
  def returns(self, book_isbn: str) -> None:
      return self.books_collection.document(book_isbn).update({u"free": True})
  
  def get_borrowed_books(self, user_id: str) -> list[Borrowing]:
    user = self.users_collection.document(user_id).get().to_dict()
    borrowed_books = user.get("borrowed_books", [])
    return [toEntity(b) for b in borrowed_books]
    





