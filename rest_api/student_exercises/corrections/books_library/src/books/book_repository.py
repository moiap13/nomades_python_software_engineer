import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from firebase_admin.firestore import DocumentSnapshot

from config.firestore_db import db

from .book import Book
from .book_mapper import BookMapper
from .book_exception import BookNotFound

class BookRepository:
  def __init__(self) -> None:
    self.collection = db.collection(u"books")
  
  def create_book(self, book: Book) -> Book:
    _, book_ref = self.collection.add(BookMapper.to_dict(book, True))
    book.id = book_ref.id
    return book
  
  def get_all(self) -> list[Book]:
    return [BookMapper.to_book(bookSnapShot) for bookSnapShot in self.collection.get()]

  def get_book_by_isbn(self, isbn: str) -> Book:
    books = self.collection.where("isbn", "==", isbn).get()
    if len(books) == 0: 
      raise BookNotFound(f"No such book with isbn={isbn}")

    return BookMapper.to_book(books[0])

if __name__ == "__main__":
  b = Book("", "test manual insert", "1234567890", ["Antonio Pisanello"])
  br = BookRepository()
  print(br.create_book(b))