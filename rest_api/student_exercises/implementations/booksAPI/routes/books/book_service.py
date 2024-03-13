from .book_repository import BookRepository
from .book import Book

class BookService():
  def __init__(self):
    self.book_repository = BookRepository()

  def get_all(self) -> list[dict]:
    return [b.to_dict() for b in self.book_repository.get_all()]
  
  def create_new_book(self, book_dto):
    b = Book.from_dto(book_dto)
    self.book_repository.insert_book(b)
    return book_dto