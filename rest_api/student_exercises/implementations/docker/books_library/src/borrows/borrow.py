import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from datetime import datetime

from src.books.book import Book
from src.users.user import User

class Borrow:
  def __init__(
    self,
    id: str = "",
    user: User = None,
    book: Book = None,
    start: datetime = None,
    end: datetime = None
  ) -> None:
    self.id = id
    self.user = user
    self.book = book
    self.start = start
    self.end = end
  
  def __str__(self) -> str:
    return f"Borrow(id={self.id}, user={self.user}, book={self.book}, start={self.start}, end={self.end})"
  
  def __repr__(self) -> str:
    return self.__str__()