from flask import g

from .borrow_repository import BorrowRepository

from routes.books.book_service import BookService
from routes.books.book import Book

class BorrowService:
  def __init__(self) -> None:
    self.book_service = BookService()
    self.repository = BorrowRepository()
  
  def get_my_borrows(self) -> list[Book]:
    my_borrows: list[dict] = self.repository.get_borrowings_by_user_id(g.user_id)

    books: list[Book] = []
    for borrow in my_borrows:
      try:
        books.append(self.book_service.get_one(borrow["book_id"]))
      except ValueError as e:
        continue
        
    return books
    
