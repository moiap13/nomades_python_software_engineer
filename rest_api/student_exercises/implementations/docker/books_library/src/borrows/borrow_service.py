import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from src.users.user_service import UserService
from src.books.book_service import BookService

from .borrow_repository import BorrowRepository
from .borrow import Borrow

class BorrowService:
  def __init__(self):
    self.repository = BorrowRepository()
    self.user_service = UserService()
    self.book_service = BookService()

  def get_borrows_per_user(self, user_id: str) -> list[Borrow]:
    return self.repository.get_borrows_per_user(user_id)

  def borrow(self, borrow_request: Borrow) -> Borrow:
    borrow_request.user = self.user_service.get_user_by_id(borrow_request.user.id)
    borrow_request.book = self.book_service.get_book_by_id(borrow_request.book.id)

    return self.repository.borrow(borrow_request)