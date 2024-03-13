import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

from config.database import db

from .book import Book

class BookRepository():
  def __init__(self):
    self.collection = db.collection(u"books")
  
  def get_all(self) -> list[Book]:
    books = self.collection.get()
    books_ret = []
    for book in books:
      bd = book.to_dict()
      assert "title" in bd and "summary" in bd
      books_ret.append(Book(book.id, bd["title"], bd["summary"]))
    return books_ret
  
  def insert_book(self, book: Book) -> None:
    self.collection.document(book.isbn).set(book.to_dict())