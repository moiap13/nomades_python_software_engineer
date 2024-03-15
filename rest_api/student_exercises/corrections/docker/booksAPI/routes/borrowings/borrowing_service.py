from flask import g
from datetime import timedelta

from .borrowing_repository import BorrowingRepository
from .borrowing import Borrowing

class BorrowingService():
  def __init__(self):
    self.borrowing_repository = BorrowingRepository()

  def borrows(self, book_isbn: str, nb_days: int) -> Borrowing:
    user_id = g.user_id
    delta_time_var = timedelta(days=nb_days) 
    return self.borrowing_repository.borrows(user_id, book_isbn, delta_time_var)
  
  def returns(self, book_isbn: str) -> None:
    return self.borrowing_repository.returns(book_isbn)
  
  def get_borrowed_books(self) -> list[Borrowing]:
    user_id = g.user_id
    return self.borrowing_repository.get_borrowed_books(user_id)