import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

from utils.google_books_api import google_books_get_by_isbn

from .book_repository import BookRepository
from .book import Book

class BookService():
  def __init__(self):
    self.book_repository = BookRepository()

  def get_all(self) -> list[dict]:
    return [b.to_dict() for b in self.book_repository.get_all()]
  
  def create_new_book(self, book_dto) -> dict | Book:
    b = Book.from_dto(book_dto)
    try:
      google_book = google_books_get_by_isbn(b.isbn)
    except Exception as e:
      google_book = None

    if google_book:
      authors = google_book["items"][0]["volumeInfo"]["authors"]
      b.authors = authors

    self.book_repository.insert_book(b)
    return b.to_dict()
  
  def get_one(self, isbn) -> Book:
    return self.book_repository.get_one(isbn)
  
  def update_one(self, isbn, book: Book) -> Book:
    f_book = self.book_repository.get_one(isbn).update(book)
    self.book_repository.update_one(f_book.isbn, f_book)
    return f_book
  
  def delete_one(self, isbn) -> None:
    return self.book_repository.delete_one(isbn)