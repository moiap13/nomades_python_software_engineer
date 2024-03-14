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
  
  def get_one(self, isbn) -> Book:
    return self.book_repository.get_one(isbn)
  
  def update_one(self, isbn, book: Book) -> Book:
    f_book = self.book_repository.get_one(isbn).update(book)
    self.book_repository.update_one(f_book.isbn, f_book)
    return f_book
  
  def delete_one(self, isbn) -> None:
    return self.book_repository.delete_one(isbn)